def app():
    import streamlit as st
    import pandas as pd
    import os

    #make a title for your webapp
    st.title("Employee Form")

    #lets try a both a text input and area as well as a date
    name = st.text_input('Full Name')
    eid = st.text_input('Employee ID')
    dept = st.text_input('Department Name')
    sal = st.text_input('Salary') 
    address = st.text_area("Address")
    mob_no = st.text_input('Mobile Number')

    header = ['Employee_ID', 'Name', 'Department', 'Salary', 'Address', 'Mobile_Number']

    clickSubmit = st.button('Submit')
    if clickSubmit == True:
        if(os.path.isfile(st.secrets["information_file"])):
            df = pd.read_csv(st.secrets["information_file"])
            id_list = df['Employee_ID'].tolist()
            if(int(eid) in id_list):
                st.error("Please enter a unique Employee ID.")
            else:
                data = [eid, name, dept, sal, address, mob_no]
                st.markdown('<h3>Thank you for your feedback!</h3>', unsafe_allow_html=True)
                file = open(st.secrets["information_file"], 'a')
                file.write(','.join(data))
                file.write("\n")
                file.close()
        else:
            data = [eid, name, dept, sal, address, mob_no]
            st.markdown('<h3>Thank you for your feedback!</h3>', unsafe_allow_html=True)
            file = open(st.secrets["information_file"], 'a')
            file.write(','.join(header))
            file.write("\n")
            file.write(','.join(data))
            file.write("\n")
            file.close()
    else:   
        st.markdown("Click submit to save form responses.")
