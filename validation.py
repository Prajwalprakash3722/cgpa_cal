####################################################################################################################################################################
# Author: Prajwal Prakash
# Date: 02/03/2021
# Goal: To calculate the approximate and provisional SGPA.
# licensed under MIT
# If you want to build the same app for your college feel free to fork it from my repo and make the necessary changes, But attriubution
# to the handle @Prajwalprakash3722 in GitHub.
###################################################################################################################################################################
import streamlit as st
import pandas as pd
from PIL import Image as im
import regex as re
from multiapp import MultiApp

app = MultiApp()

def app():
    logo = im.open("rvce.png")
    st.image(logo)
    st.title("RV College Of Engineering cgpa calculator: (Beta stage) ")
    st.write("Only for First Year Students")
    st.markdown(
    "This platform is developed and deployed by **Prajwal Prakash, CSE department'24**")

    name = st.text_input("Enter Your name: ")
    email = st.text_input("Enter your college-email: ")
    verified_email = re.search("20@rvce.edu.in", email)
    if st.button("Enter"):
        if verified_email:
            st.markdown("You are verified")
            st.sidebar.markdown(
                            """<a href="https://share.streamlit.io/prajwalprakash3722/cgpa_cal/main/cgpa.py">Go ahead</a>""", unsafe_allow_html=True,)
            app.add_app(
                "RV College Of Engineering cgpa calculator: (Beta stage)", cgpa.app)
        else:
            st.write("Enter your correct email address....")
app()