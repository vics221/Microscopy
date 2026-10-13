"""Streamlit wrapper: embeds the browser-based ND2 viewer (index.html).

The viewer runs entirely in the user's browser, so .nd2 files are read locally:
nothing is uploaded to the Streamlit server and the 200 MB upload limit does not apply.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ND2 viewer", layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>.block-container{padding:0.5rem 0.5rem 0 0.5rem}header{visibility:hidden}</style>",
            unsafe_allow_html=True)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=1800, scrolling=True)
