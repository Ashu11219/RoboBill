import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key= "AIzaSyDr7LZNa8zNTZrOyp2sqWNi6mM9QFTPeoQ")

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text, image_data, prompt):
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file was uploaded")

#Page design
st.set_page_config(page_title= "AM's Invoice Generator")
st.sidebar.header("RoboBill")
st.sidebar.write('Made by Ashish')
st.sidebar.write('Powered by google Gemini AI')
st.header('RoboBill')
st.subheader('Made by Ashish')
st.subheader('Manage your expenses with RoboBill')

input = st.text_input('What do you want me to do?', key= 'input')
uploaded_file = st.file_uploader('Choose an image', type= ['jpg', 'jpeg', 'png', 'heic'])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption= 'Uploaded Image', use_column_width= True)

ssubmit = st.button('Start the search!')

input_prompt = """
You are an expert in reading invoices, We are going to upload an image of an invoice and
you will have to answer any type of questions that the user asks you.
You have to greet the user politely first. Make sure to keep the fonts uniform and give the items list in
a point-wise format.
At the end, make sure to repeat the name of our app "RoboBill" and ask the user to use it again
"""
if ssubmit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("Here's what you need to know")
    st.write(response)
