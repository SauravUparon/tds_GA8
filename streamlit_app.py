import streamlit as st

st.title("Greatest among the 3 numbers")

num1 = st.number_input("Input First Number", format="%g")
num2 = st.number_input("Input Second Number", format="%g")
num3 = st.number_input("Input third Number", format="%g")

largest = max(num1,num2,num3)
if st.button("Find"):
    st.write("Greatest among the 3 numbers {},{} and {} is {}".format(num1,num2,num3,largest))
