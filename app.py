import save_info
import extract_info
import update_info
import streamlit as st
PAGES = {
    "Save Info": save_info,
    "Extract Info": extract_info,
    "Update Info": update_info
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()