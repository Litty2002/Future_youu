import streamlit as st

from login_manager import Users

#title
st.title("Welcome to :red[Future You] ")
#login signup
choice = st.selectbox("Login/Signup",["Login","Signup"], key='log_choice')
#for login
if choice=="Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password",type='password')
    if st.button("Login"):
        with Users() as users:
            if users.check_user(username, password):
                st.switch_page("pages/app.py")
            else:
                st.warning("Incorrect Username/Password")

   
#for signup
else:
    st.subheader("Sign Up ")
    email = st.text_input("Email Address")
    username = st.text_input("Enter your username")
    password = st.text_input("Password",type='password')

    
    if st.button("Create my account"):
        with Users() as user:
            user.add_user(username, password)
        st.success("Successfully created the acoount {}".format(username))
        st.switch_page("pages/app.py")
