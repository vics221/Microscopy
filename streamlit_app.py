from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ND2 viewer", layout="wide", initial_sidebar_state="collapsed")

if "ok" not in st.session_state:
    st.session_state.ok = False

if not st.session_state.ok:
    pw = st.text_input("Password", type="password")
    if pw:
        if pw == st.secrets["APP_PASSWORD"]:
            st.session_state.ok = True
            st.rerun()
        else:
            st.error("Wrong password")
    st.stop()

st.markdown("<style>.block-container{padding:0.5rem 0.5rem 0 0.5rem}header{visibility:hidden}</style>",
            unsafe_allow_html=True)
html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=1800, scrolling=True)
