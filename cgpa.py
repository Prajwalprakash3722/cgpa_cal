####################################################################################################################################################################
# Author: Prajwal Prakash
# Date: 02/03/2021
# Goal: To calculate the approximate and provisional SGPA.
# licensed under MIT
# If you want to build the same app for your college feel free to fork it from my repo and make the necessary changes, But attriubution
# to the handle @Prajwalprakash3722 in GitHub is mandaotry
###################################################################################################################################################################
import streamlit as st
import pandas as pd
from PIL import Image as im

def app():
    logo = im.open("rvce.png")
    st.image(logo)
    st.title("RV College Of Engineering cgpa calculator: (Beta stage)")
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
        ('Aerospace Engineering',
        
        'Biotechnology',

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
            sub = st.selectbox("Select the Subject which you want the grade to be calculated ?",
                           ('Engineering Mathematics 18MA11',

                            'Engineering Chemistry 18CH12',

                            'Programming in C 18CS13',

                            'Elements of Electronics 18EC14',

                            'Elements of Mechanical Engineering 18ME15',

                            'English Lab 18HS16'))
        else:
            sub = st.selectbox("Select the Subject which you want the grade to be calculated ?",
                           ('Engineering Mathematics 18MA21',

                            'Engineering Chemistry 18CH22',

                            'Programming in C 18CS23',

                            'Elements of Electronics Engineering 18EC24',

                            'Elements of Mechanical Engineering 18ME25',

                            'English Lab 18HS26'))

    else:
        st.write("You have 7 Subjects. ")
        if sem == '1st Sem':
            sub = st.selectbox("Select the Subject which you want the grade to be calculated ?",
                               ("Engineering Mathematics 18MA11",

                                "Engineering Physics 18PH12",

                                "Elements of Electrical Engineering 18EE13"
                                "Elements of Engineering Practices 18EE15",

                                 "Computer Aided Engineering Drawing 18ME16",

                                 "English Lab 18HS17",

                                 "Elements of Civil Engineering and Mechanics 18CV14"))

        else:
            sub = st.selectbox("Select the Subject which you want the grade to be calculated ?",
                               ("Engineering Mathematics 18MA21",

                                "Engineering Physics 18PH22",

                                "Elements of Electrical Engineering 18EE23"
                                "Elements of Engineering Practices 18EE25",

                                 "Computer Aided Engineering Drawing 18ME26",

                                 "English Lab 18HS27",

                                 "Elements of Civil Engineering and Mechanics 18CV24"))

    st.title("CIE Marks")
    st.write(
        "Imp-Point:\n The Experiential marks are assumed to be 18 in each subject")
    st.write("For", sub)
    cie_1 = int(st.number_input("Enter the 1st internal marks: "))
    quiz_1 = st.number_input("Enter the 1st Quiz marks: ")
    if cie_1 > 50 or quiz_1 > 10:
        st.write("Enter correct marks of CIE-1.")
    cie_2 = int(st.number_input("Enter the 2nd internal marks: "))
    quiz_2 = st.number_input("Enter the 2nd Quiz marks: ")
    if cie_2 > 50 or quiz_2 > 10:
        st.write("Enter correct marks of CIE-2.")
    cie_3 = st.number_input("Enter the 3rd internal marks: ")
    quiz_3 = st.number_input("Enter the 3rd Quiz marks: ")
    if cie_3 > 50 or quiz_3 > 10:
        int(st.write("Enter correct marks of CIE-3."))
    if st.button("Calculate"):
        cie_avg = int((cie_1 + cie_2 + cie_3) / 3.0)
        quiz_total = quiz_1 + quiz_2 + quiz_3
        if cie_1 and cie_2 and cie_3 > 21:
            #st.image('/congo.png')
            st.write("Congratulations You have passed in ", sub)
            st.write("Total Average Internal Marks : ", cie_avg)
            st.write("Total Quiz marks in", sub, "is: ", quiz_total)
            total_marks = quiz_total + cie_avg + 18
            if total_marks > 90:
                grades = 'S'
            elif total_marks > 80 or total_marks < 90:
                grades = 'A'
            elif total_marks > 70 or total_marks < 80:
                grades = 'B'
            elif total_marks > 60 or total_marks < 70:
                grades = 'C'
            st.write("You have been awarded '", grades, "' Grades", ", Total marks: ", total_marks)
        else:
            st.markdown("Enter Correct marks!!! (Fill all the fields)")
app()