import streamlit as st
import streamlit.components.v1 as components
# https://github.com/sfc-gh-jbukhari/prayertimes.git
# st.write("true")
html_render="true - this is prayer time now ..... "
components.html(html_render, scrolling=True, height=1200)
