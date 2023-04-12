import streamlit as st
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title="Main Menu",
    options=["Home", "Image", "Video"],
    icons=["house","card-image", "camera-video"],
    orientation="horizontal",    
)

if selected == "Home":
    st.title(f"Hello! I am Kritika Sureka from the department of Electronics and Telecommunications")
if selected == "Image":
   option = st.selectbox('Please upload an image',('Upload a file', 'Use Camera'))
   if option == "Upload a file":
     images=st.file_uploader("Please uplaod an image", type=["png", "jpg", "jpeg", "gif"], accept_multiple_files=True)
     if images is not None:
         for image in images:
            st.image(image)
   if option == "Use Camera":    
      picture = st.camera_input("Take a picture")
      if picture:
        st.image(picture)
if selected == "Video":
    videos=st.file_uploader("Please uplaod a video", type=["mp4", "mov", "wmv", "flv"], accept_multiple_files=True)
    if videos is not None:
        for video in videos:
         st.video(video)
    
    
   