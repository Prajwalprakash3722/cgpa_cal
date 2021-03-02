import streamlit as st
import pandas as pd
from PIL import Image as im

logo = im.open("rvce.png")
st.image(logo)
st.title("RV College Of Engineering grade calculator: ")
st.write("Only for First Year Students")
st.markdown("This platform is developed and deployed by Prajwal Prakash, CSE department'24 ")

cycle = st.radio(
    "Select the cycle in which you are in ?",
    ('P-cycle', 'C-cycle'))
if cycle == 'P-cycle':
    st.write('You selected P-cycle.')
else:
    st.write("You selected C-cycle.")
sem = st.selectbox("Select the sem  that you are in: ",
                   ("1st Sem", "2nd Sem"))
branch = st.selectbox(
    "Select the branch that you are in ?",
    ('Biotechnology',

     'Chemical Engineering',

     'Civil Engineering',

     'Computer Science & Engineering',

     'Electrical & Electronics',

     'Electronics & Communication',

     'Instrumentation Technology',

     'Industrial Engineering & Management',

     'Information Science & Engineering',

     'Mechanical Engineering',

     'Telecommunication Engineering'))

if cycle == 'C-cycle':
    st.write("You have 6 Subjects. ")
    if sem == "1st Sem":
        subject = st.radio(
            "Select the Subject which you want the grade to be calculated ?",
            ('Engineering Mathematics 18MA11', 'Engineering Chemistry 18CH12',
             'Programming in C 18CS13', 'Elements of Electronics 18EC14',
             'Elements of Mechanical Engineering 18ME15', 'English Lab 18HS16'))
    elif sem == "2nd Sem":
        subject = st.radio(
            "Select the Subject which you want the grade to be calculated ?",
            ('Engineering Mathematics 18MA11', 'Engineering Chemistry 18CH12',
             'Programming in C 18CS13', 'Elements of Electronics 18EC14',
             'Elements of Mechanical Engineering 18ME15', 'English Lab 18HS16'))

else:
    st.write("You have 7 Subjects. ")
    if sem == '1st Sem':
        subject = st.radio("Select the Subject which you want the grade to be calculated ?",
                           ("Engineering Mathematics 18MA11", "Engineering Physics 18PH12",
                            "Elements of Electrical Engineering 18EE13",
                            "Elements of Civil Engineering and Mechanics 18CV14",))
        subject2 = st.radio("",
                            ("Elements of Engineering Practices 18EE15", "Computer Aided Engineering Drawing 18ME16",
                             "English Lab 18HS17"))

    else:
        subject = st.radio("Select the Subject which you want the grade to be calculated ?",
                           ("Engineering Mathematics 18MA21", "Engineering Physics 18PH22",
                            "Elements of Electrical Engineering 18EE23",
                            "Elements of Civil Engineering and Mechanics 18CV24",))
        subject2 = st.radio("",
                            ("Elements of Engineering Practices 18EE25", "Computer Aided Engineering Drawing 18ME26",
                             "English Lab 18HS267"))


def cie():
    cie_1 = st.number_input("Enter the 1st internal marks: ")
    cie_2 = st.number_input("Enter the 2nd internal marks: ")
    cie_3 = st.number_input("Enter the 3rd internal marks: ")
    cie_avg = (cie_1 + cie_2 + cie_3) / 3.0
    st.write("Average Internal Marks : ", cie_avg)


cie()
