import streamlit as st
import pandas as pd
from PIL import Image as im


logo = im.open("rvce.png")
st.image(logo)
st.title("RV College Of Engineering cgpa calculator: (Beta stage) ")
st.write("Only for First Year Students")
st.markdown(
    "This platform is developed and deployed by **Prajwal Prakash, CSE department'24**")
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
    if sem == '1st Sem':
        sub = st.radio("Select the Subject which you want the grade to be calculated ?",
                       ('Engineering Mathematics 18MA11',

                        'Engineering Chemistry 18CH12',

                        'Programming in C 18CS13',

                        'Elements of Electronics 18EC14',

                        'Elements of Mechanical Engineering 18ME15',

                        'English Lab 18HS16'))
    else:
        sub = st.radio("Select the Subject which you want the grade to be calculated ?",
                       ('Engineering Mathematics 18MA21',

                        'Engineering Chemistry 18CH22',

                        'Programming in C 18CS23',

                        'Elements of Electronics 18EC24',

                        'Elements of Mechanical Engineering 18ME25',

                        'English Lab 18HS26'))

else:
    st.write("You have 7 Subjects. ")
    if sem == '1st Sem':
        subject = st.radio("Select the Subject which you want the grade to be calculated ?",
                           ("Engineering Mathematics 18MA11",

                            "Engineering Physics 18PH12",

                            "Elements of Electrical Engineering 18EE13",
                            "0",))
        subject2 = st.radio("",
                            ("Elements of Engineering Practices 18EE15",

                             "Computer Aided Engineering Drawing 18ME16",

                             "English Lab 18HS17",

                             "Elements of Civil Engineering and Mechanics 18CV14"))

    else:
        subject = st.radio("Select the Subject which you want the grade to be calculated ?",
                           ("Engineering Mathematics 18MA21",

                            "Engineering Physics 18PH22",

                            "Elements of Electrical Engineering 18EE23",
                            "0",))
        subject2 = st.radio("",
                            ("Elements of Engineering Practices 18EE25",

                             "Computer Aided Engineering Drawing 18ME26",

                             "English Lab 18HS27",

                             "Elements of Civil Engineering and Mechanics 18CV24"))

    if subject == "0":
        sub = subject2
    else:
        sub = subject

st.title("CIE Marks")
st.write("For", sub)
cie_1 = int(st.number_input("Enter the 1st internal marks: "))
if cie_1 > 50:
    st.write("Enter correct marks of CIE-1.")
cie_2 = int(st.number_input("Enter the 2nd internal marks: "))
if cie_2 > 50:
    st.write("Enter correct marks of CIE-2.")
cie_3 = st.number_input("Enter the 3rd internal marks: ")
if cie_3 > 50:
    int(st.write("Enter correct marks of CIE-3."))
if st.button("Calculate"):
    cie_avg = int((cie_1 + cie_2 + cie_3) / 3.0)
    if cie_1 and cie_2 and cie_3 > 21:
        st.image('/home/prajwal/projects/cgpa_calc/congo.png')
        st.write("Congratulations You have passed in ", sub)
        st.write("Total Average Internal Marks : ", cie_avg)
st.title("SEE Marks")
see_marks = int(st.number_input("Enter the External examination marks: "))
if see_marks > 100:
    st.write("Enter correct marks of SEE.")
    date = st.date_input("Enter the date: ")
cie_avg = int((cie_1 + cie_2 + cie_3) / 3.0)
if see_marks >= 90 and (cie_avg > 21):
    grade = 10
elif see_marks >= 80 and (cie_avg > 21):
    grade = 9
elif see_marks >= 70 and (cie_avg > 21):
    grade = 8
elif see_marks >= 60 and (cie_avg > 21):
    grade = 7
elif see_marks >= 50 and (cie_avg > 21):
    grade = 6
elif see_marks >= 50 and (cie_avg > 21):
    grade = 5
else:
    grade = "F"

if st.button("submit"):
    st.write("You have been awarded", grade, "grades")

if st.button("CIE-report"):
    df = [cie_1, cie_2, cie_3, cie_avg]
    st.bar_chart(df, width=0, height=0)
if st.button("Do You want to rate this Service ? "):
    rate = int(
        st.select_slider('How do You rate this service', options=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']))
    rate += rate
