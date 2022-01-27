def app():
    import streamlit as st
    import pandas as pd

    #make a title for your webapp
    st.title("View Information")

    #lets try a both a text input and area as well as a date
    eid = st.text_input('Employee ID')

    clickSubmit = st.button('Submit')

    if clickSubmit == True:
        df = pd.read_csv('user.txt')
        res = (df[df['Employee_ID'] == int(eid)])
        st.dataframe(res)

    else:
        st.markdown("Click submit to save form responses.")
