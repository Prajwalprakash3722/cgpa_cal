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
import streamlit.components.v1 as components

def app():
    logo = im.open("rvce.png")
    st.image(logo)
    st.title("RV College Of Engineering cgpa calculator: (Beta stage)")
    st.write("Only for First Year Students")
    st.markdown(
        "This platform is developed and deployed by **Prajwal Prakash, CSE department'24**")


def cgpa():
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

                                "Elements of Electrical Engineering 18EE13",
                                "Elements of Engineering Practices 18EE15",

                                "Computer Aided Engineering Drawing 18ME16",

                                "English Lab 18HS17",

                                "Elements of Civil Engineering and Mechanics 18CV14"))

        else:
            sub = st.selectbox("Select the Subject which you want the grade to be calculated ?",
                               ("Engineering Mathematics 18MA21",

                                "Engineering Physics 18PH22",

                                "Elements of Electrical Engineering 18EE23",
                                "Elements of Engineering Practices 18EE25",

                                "Computer Aided Engineering Drawing 18ME26",

                                "English Lab 18HS27",

                                "Elements of Civil Engineering and Mechanics 18CV24"))

    st.title("CIE Marks")
    st.write(
        "Imp-Point:\n The Experiential Learning marks are assumed to be 18 in each subject, If you want to change it click here")
    el = st.checkbox("Change Experiential Learning marks")
    if el:
        experiential_learning_marks = st.number_input(
            "Enter your experiential learning marks: ")
        if experiential_learning_marks > 20:
            st.write("Enter correct marks")
    else:
        experiential_learning_marks = 18
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
    lab_internals = st.number_input(
        "Enter the lab CIE marks (for the subjects that don't have lab you can type 50): ")
    if st.button("Calculate"):
        cie_avg = int((cie_1 + cie_2 + cie_3) / 3.0)
        quiz_total = quiz_1 + quiz_2 + quiz_3
        if cie_1 and cie_2 and cie_3 > 21:
            logo_cong = im.open("congo.png")
            st.image(logo_cong)
            total_marks = quiz_total + cie_avg + experiential_learning_marks + lab_internals
            total_marks_final = (2*total_marks)//3
            if total_marks_final > 90:
                grades = 'S'
            elif total_marks_final > 80 or total_marks < 90:
                grades = 'A'
            elif total_marks_final > 70 or total_marks < 80:
                grades = 'B'
            elif total_marks_final > 60 or total_marks < 70:
                grades = 'C'
            st.header("Report")
            st.write("Cycle: ", cycle)
            st.write("Branch: ", branch)
            st.write("Semester: ", sem)
            st.write("Sub: ", sub)
            st.write("Total CIE average: ", cie_avg)
            st.write("Total Quiz: ", quiz_total)
            st.write("Grades: ", grades)
            st.write("Total marks: ", total_marks, "out of 150")
            st.write("Final marks: ", total_marks_final, "out of 100")
        else:
            st.markdown("Enter Correct marks!!! (Fill all the fields)")
    st.markdown(
        """Developed by <a href="https://prajwalprakash3722.github.io/prajwalsportfolio/">_introverted_coder_</a>""", unsafe_allow_html=True,)

    st.markdown(
        "Any Issues, Just tweet it and mention me, I'll try my best to address them")
    components.html("""<a href="https://twitter.com/intent/tweet?screen_name=prakash_prajwal&ref_src=twsrc%5Etfw" class="twitter-mention-button" data-lang="en" data-show-count="false">Tweet to @prakash_prajwal</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>""")
app()
cgpa()
