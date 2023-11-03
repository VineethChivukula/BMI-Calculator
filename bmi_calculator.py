import streamlit as st
import sys

# Define the webpage title
st.title("BMI Calculator")

# Add the input controls to the webpage
name = st.text_input("Name:")
gender = st.radio("Gender:", ("Male", "Female", "Other"))
age = st.number_input("Age:", min_value=0, max_value=120)
address = st.text_area("Address:")
hobbies = ["Reading", "Sports", "Music", "Art"]
hobbies_selected = []
for hobby in hobbies:
    if st.checkbox(hobby):
        hobbies_selected.append(hobby)
weight = st.number_input("Weight in kg:", min_value=0, max_value=500)
height = st.number_input("Height in cm:", min_value=0, max_value=300)
if(age<=0):
        st.write("Please Enter Correct Age")
if(name is None):
        st.write("Please Enter Your Name")
try:
    bmi = weight / (height_m ** 2)
except ZeroDivisionError as e:
    st.write("Please Enter Your Height")
    sys.exit(1)
    
# Retrieve the user's personal details and Calculate BMI
if st.button("Submit"):
    st.write("Name:", name)
    st.write("Gender:", gender)
    st.write("Age:", age)
    st.write("Address:", address)
    st.write("Hobbies:", hobbies_selected)
    st.write("Weight:", weight)
    st.write("Height:", height)
    height_m = height / 100
    st.write("Your BMI is: {:.2f}".format(bmi))
    if bmi < 18.5:
        st.write("You are underweight")
    elif bmi >= 18.5 and bmi < 25:
        st.write("You are normal weight")
    elif bmi >= 25 and bmi < 30:
        st.write("You are overweight")
    else:
        st.write("You are obese")
