import streamlit as st


def footer_home():
    logo_url = "class.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created By shivam kumar </p>  
        <img src='shivam.png' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown(
        """
        <div style="text-align:center; padding:2rem 0; color:#666;">
            © 2026 ClassMate AI
        </div>
        """,
        unsafe_allow_html=True,
    )