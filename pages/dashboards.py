import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
import streamlit.components.v1 as components

st.title("Power BI Report")

# Your working iframe embedded as raw HTML
components.html(
    """
    <iframe title="clean" width="1140" height="541.25"
        src="https://app.powerbi.com/reportEmbed?reportId=80a3c2d5-5ae0-4bef-a89e-f0cb8718888f&autoAuth=true&embeddedDemo=true"
        frameborder="0" allowFullScreen="true"></iframe>
    """,
    height=550 
)
