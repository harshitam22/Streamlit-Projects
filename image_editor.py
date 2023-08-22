import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style='text-align:center;'> Image Editor </h1>" , unsafe_allow_html=True)
st.markdown("---")
image = st.file_uploader("Upload Your Image" , type=["jpg" , "jpeg" , "png"])
info = st.empty() 
size = st.empty()
mode = st.empty()
format_ = st.empty()

if image:
    img = Image.open(image)
    info.markdown("<h1 style='text-align:center;'> Information </h1>" , unsafe_allow_html=True)
    size.markdown(f"<h6>Size: {img.size}</h6>",unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode: {img.mode}</h6>",unsafe_allow_html=True)
    format_.markdown(f"<h6>Size: {img.format}</h6>" , unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align:center;'> Resizing </h1>" , unsafe_allow_html=True)
    width = st.number_input("width" , value=img.width)
    height = st.number_input("height" , value=img.height)

    st.markdown("<h1 style='text-align:center;'> Rotation </h1>" , unsafe_allow_html=True)
    degree = st.number_input("Degree")

    st.markdown("<h1 style='text-align:center;'> Filters </h1>" , unsafe_allow_html=True)
    filters = st.selectbox("Filters" , options = ["None" , "Blur"  , "Embosss" , "Detail" , "Smooth"])

    s_btn = st.button("Apply")
    if s_btn:
        edited = img.resize((width , height)).rotate(degree)
        filtered = edited
        if filters != "None":
            if filters == "Blur":
                filtered = edited.filter(BLUR)
            elif filters == "Emboss":
                filtered = edited.filter(EMBOSS)
            elif filters == "Detail":
                filtered = edited.filter(DETAIL)
            else:
                filtered = edited.filter(SMOOTH)            
        st.image(filtered)
