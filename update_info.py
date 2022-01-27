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
            new_address = st.text_input('Enter New Address')
    elif option_2:
        new_mob_num = st.text_input('Enter New Mobile number')

    clickSubmit = st.button('Update')
    if clickSubmit == True:
        df = pd.read_csv('user.txt')
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
        df.set_index('Employee_ID', inplace=True)
        df.update(res.set_index('Employee_ID'))
        df.reset_index(inplace=True)
        df.to_csv('user.txt', index=None, sep=',')
        print(df)
