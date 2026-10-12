import base64
from pathlib import Path

import streamlit as st


def header_home():
    logo_path = Path(__file__).parent / "image" / "class.png"
    logo_url = "data:image/png;base64," + base64.b64encode(
        logo_path.read_bytes()
    ).decode("ascii")

    st.markdown(
        f"""
        <div style="display:flex; flex-direction:column; align-items:center;
                    justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src="{logo_url}" style="height:100px;">
            <h1 style="text-align:center;">ClassMate.ai</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )


def header_dashboard():
    st.title("ClassMate AI")