import regex as re
import streamlit as st


def regex_validation():
    name = st.text_input("Enter Your name: ")
    email = st.text_input("Enter your college-email: ")
    verified_email = re.search("20@rvce.edu.in", email)
    if st.button("Enter"):
        if verified_email:
            st.markdown("You are verified")
            cgpa()
        else:
            st.write("Enter your correct email address....")


regex_validation()
