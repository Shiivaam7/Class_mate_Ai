# 🎓 ClassMate AI — Smart Attendance & Classroom Management

**ClassMate AI** is an AI-powered classroom management project designed to simplify student attendance management using face recognition and a web-based interface.

🌐 **Live Demo:** [ClassMate AI](https://classmate-main.streamlit.app/)  
💻 **GitHub Repository:** [ClassMate AI on GitHub](https://github.com/Shiivaam7/Class_mate_Ai)

---

## 📌 Overview

Managing classroom attendance manually can be time-consuming and inefficient. ClassMate AI aims to make this process smarter by combining a web application with a face-recognition-based attendance workflow.

The project includes separate teacher and student interfaces to support classroom-related operations.

## ✨ Features

- **Teacher Portal:** Teacher registration and login functionality.
- **Student Portal:** A dedicated interface for students.
- **Face Recognition:** A face-recognition pipeline for attendance processing.
- **Attendance Management:** Designed to support digital attendance records.
- **Database Integration:** Uses Supabase for database connectivity.
- **Web Interface:** Built with Streamlit for an interactive application experience.

*Note: Feature availability depends on the current application configuration and database setup.*

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Supabase | Database and backend services |
| Face Recognition | Face-based attendance workflow |
| Git & GitHub | Version control and source code management |

## 🏗️ Project Structure

```text
Class_mate_Ai/
│
├── app.py
├── src/
│   ├── database/
│   │   ├── config.py
│   │   └── db.py
│   ├── pipeline/
│   │   └── face_pipeline.py
│   └── screen/
│       ├── teacher_screen.py
│       └── student_screen.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

*The structure above is based on the project modules identified so far. Update it if your repository contains additional files or folders.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Shiivaam7/Class_mate_Ai.git
cd Class_mate_Ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment secrets

Create a `.streamlit/secrets.toml` file and add your Supabase credentials:

```toml
SUPABASE_URL = "your_supabase_project_url"
SUPABASE_KEY = "your_supabase_publishable_key"
```

Replace the placeholder values with your own credentials. These names must match the keys used in your application code.

**Security:** Never commit `secrets.toml`, passwords, or private service-role keys to GitHub. Configure deployment secrets separately in Streamlit Community Cloud.

### 5. Run the application

```bash
streamlit run app.py
```

The application should open in your browser at the local Streamlit address shown in the terminal.

## 🗄️ Database Configuration

ClassMate AI uses Supabase for database connectivity.

Before running the application:

1. Create or select a Supabase project.
2. Configure the database tables and columns expected by the application.
3. Configure appropriate Row Level Security (RLS) policies.
4. Add the required credentials to your local secrets file.
5. Verify that teacher and student database operations work correctly.

The exact database schema should match the queries implemented in the project's database modules.

## 🚀 Deployment

The application is deployed using Streamlit Community Cloud.

**Live Application:** https://classmate-main.streamlit.app/

To deploy your own version:

1. Push the project to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub repository.
4. Select `app.py` as the application entry point.
5. Configure the required secrets.
6. Deploy and test the application.

## 🔮 Future Improvements

- Improve face-recognition accuracy and reliability.
- Add attendance reports and downloadable summaries.
- Enhance the teacher and student dashboards.
- Add stronger authentication and role-based access control.
- Improve database error handling and application reliability.
- Add attendance analytics and visual reports.

## 🎯 Project Goal

The goal of ClassMate AI is to explore how AI and web technologies can help make classroom attendance and management more efficient.

## 👨‍💻 Author

**Shivam Kumar**

GitHub: [@Shiivaam7](https://github.com/Shiivaam7)

---

⭐ If you find this project interesting, consider giving the repository a star!
