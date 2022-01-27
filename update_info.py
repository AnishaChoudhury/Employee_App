def app():
    import streamlit as st
    import pandas as pd

    #make a title for your webapp
    st.title("Update Information")
    st.markdown('**NOTE: ** _You can only update address or mobile number_.')

    eid = st.text_input('Enter the Employee ID whose data you want to update')
    st.write('Select what you want to update:')
    option_1 = st.checkbox('Address')
    option_2 = st.checkbox('Mobile Number')
    if option_1:
        if option_2:
            new_mob_num = st.text_input('Enter New Mobile number')
            new_address = st.text_input('Enter New Address')
        else:
            new_mob_num = st.text_input('Enter New Address')
    elif option_2:
        new_mob_num = st.text_input('Enter New Mobile number')

    clickSubmit = st.button('Update')
    if clickSubmit == True:
        df = pd.read_csv(st.secrets["information_file"])
        res = (df[df['Employee_ID'] == int(eid)])
        st.markdown('**The Old entry was as follows: **')
        st.dataframe(res)
        if option_1:
            if option_2:
                res['Address'] = [new_address]
                res['Mobile_Number'] = [str(new_mob_num)]
            else:
                res['Address'] = [new_address]
        elif option_2:
            res['Mobile_Number'] = [str(new_mob_num)]
        st.markdown('**The Update entry is as follows: **')
        st.dataframe(res)

        #### This is used to update the original dataframe. Set index sets employee id as the S.NO of the data frame. It makes it easy to update.
        df.set_index('Employee_ID', inplace=True)
        df.update(res.set_index('Employee_ID'))

        ### This is used to bring the original index back.
        df.reset_index(inplace=True)

        #### This is used to save csv as text file.
        df.to_csv(st.secrets["information_file"], index=None, sep=',')
