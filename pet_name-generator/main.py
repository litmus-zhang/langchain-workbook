import langchain_helper as lch
import streamlit as st


st.title('Pet Name Generator')

animal_type = st.sidebar.selectbox('What is your pet?', ("Cat", "Dog", "Cow", "Cock", "Tiger", "Hamster"))

match animal_type:
    case "Cat":
        pet_color = st.sidebar.text_area("What color is your cat", max_chars=15)
    case "Dog":
        pet_color = st.sidebar.text_area("What color is your dog ", max_chars=15)
    case "Cow":
        pet_color = st.sidebar.text_area("What color is your cow", max_chars=15)
    case "Cock":
        pet_color = st.sidebar.text_area("What color is your Cock", max_chars=15)
    case "Tiger":
        pet_color = st.sidebar.text_area("What color is your Tiger", max_chars=15)
    case "Hamster":
        pet_color = st.sidebar.text_area("What color is your Hamster", max_chars=15)


if pet_color:
    response = lch.generate_pet_name(animal_type, pet_color)
    st.text(response)