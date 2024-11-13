import streamlit as st

st.title("Welcome to My School  ")
# st.header("Welcome to Quetta  ")
# st.header("Welcome to My School ")
# st.checkbox("Is it good ")
# st.camera_input("Take a Picture ")
# st.title("The ending of this project  ")
name = st.text_input("Enter Student Name   ")
fname =st.text_input("Enter  FatherName   ")
roll = st.text_input("Enter Roll Number  ")
adr = st.text_input("Enter Your Address   ")
classdata = st.selectbox("Enter the Class :",(1,2,4,5,6,7,8,9,10))
button = st.button("Done ")
if button:
     st.markdown(f"""
                 Name : {name}
                 fathername  : {fname}
                 roll number  :  {roll}
                 adress : {adr}
                 class : {classdata}
                 """)