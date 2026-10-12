from src.database.config import supabase
import bcrypt
import logging
import re


logger = logging.getLogger(__name__)


def _log_supabase_error(operation, error):
    code = getattr(error, "code", None)
    if isinstance(code, int) and 100 <= code <= 599:
        safe_code = f"HTTP_{code}"
    elif isinstance(code, str) and re.fullmatch(r"[A-Za-z0-9_-]{1,32}", code):
        safe_code = code
    else:
        safe_code = "unavailable"
    message = str(getattr(error, "message", "")).lower()

    if "json could not be generated" in message:
        safe_message = "Supabase returned a non-standard error response; response body suppressed."
    elif "schema cache" in message or "could not find" in message:
        safe_message = "PostgREST could not resolve a requested table or column."
    elif "row-level security" in message or "row level security" in message:
        safe_message = "A row-level security policy rejected the operation."
    elif "permission denied" in message or "insufficient privilege" in message:
        safe_message = "Database permissions rejected the operation."
    elif "duplicate key" in message or "unique constraint" in message:
        safe_message = "A unique constraint rejected the row."
    elif "foreign key" in message:
        safe_message = "A foreign-key constraint rejected the row."
    elif "null value" in message or "not-null constraint" in message:
        safe_message = "A required database field was missing."
    elif "invalid input syntax" in message or "datatype mismatch" in message:
        safe_message = "A value did not match the database column type."
    else:
        safe_message = "Supabase request failed; server details suppressed."

    logger.error("Supabase %s failed (code=%s): %s", operation, safe_code, safe_message)



def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())


def check_teacher_exists(username):
    # Check for unique username, returns false when username is already taken
    try:
        response = supabase.table("teachers").select("username").eq("username", username).execute()
    except Exception as error:
        _log_supabase_error("check_teacher_exists", error)
        raise
    return len(response.data) > 0 



def create_teacher(username, password, name):

    data = { "username" : username, "password": hash_pass(password), "name": name}
    try:
        response = supabase.table("teachers").insert(data).execute()
    except Exception as error:
        _log_supabase_error("create_teacher", error)
        raise
    return response.data


def teacher_login(username, password):
    try:
        response = supabase.table("teachers").select("*").eq("username", username).execute()
    except Exception as error:
        _log_supabase_error("teacher_login", error)
        raise
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher['password']):
            return teacher
    return None


def get_all_students():
    try:
        response = supabase.table('students').select("*").execute()
    except Exception as error:
        _log_supabase_error("get_all_students", error)
        raise
    return response.data

def create_student(new_name, face_embedding=None, voice_embedding=None):
    data = {'name': new_name, 'face_embedding':face_embedding, "voice_embedding": voice_embedding}
    response = supabase.table('students').insert(data).execute()
    return response.data


def create_subject(subject_code, name, section, teacher_id):
    data = {"subject_code": subject_code, "name": name, "section": section, "teacher_id": teacher_id}
    response = supabase.table("subjects").insert(data).execute()
    return response.data

def get_teacher_subjects(teacher_id):
    response = supabase.table('subjects').select("*, subject_students(count), attendance_logs(timestamp)").eq("teacher_id", teacher_id).execute()
    subjects = response.data


    for sub in subjects:
        sub['total_students'] = sub.get("subject_students", [{}])[0].get('count', 0) if sub.get('subject_students') else 0
        attendance = sub.get('attendance_logs', [])
        unique_sessions = len(set(log['timestamp'] for log in attendance))
        sub['total_classes'] = unique_sessions


        sub.pop('subject_student', None)
        sub.pop('attendance_logs', None)

    return subjects


def  enroll_student_to_subject(student_id, subject_id):
    data = {'student_id': student_id, "subject_id": subject_id}
    response= supabase.table('subject_students').insert(data).execute()
    return response.data


def  unenroll_student_to_subject(student_id, subject_id):
    response= supabase.table('subject_students').delete().eq('student_id', student_id).eq('subject_id', subject_id).execute()
    return response.data



def get_student_subjects(student_id):
    response = supabase.table('subject_students').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def get_student_attendance(student_id):
    response = supabase.table('attendance_logs').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def create_attendance(logs):
    response = supabase.table('attendance_logs').insert(logs).execute()
    return response.data

def get_attendance_for_teacher(teacher_id):
    response = supabase.table('attendance_logs').select("*, subjects!inner(*)").eq('subjects.teacher_id', teacher_id).execute()
    return response.data