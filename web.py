import streamlit as st
from open_camera import Camera
import cv2
from PIL import Image
import os

st.set_page_config(
    page_title="V-sight",
    page_icon="v-sight.jpg",
    layout="centered",
    initial_sidebar_state="expanded"
)

tab1, tab2, tab3 = st.tabs(["realtime detection","image detection","try"])


with tab1:
    # Create an instance of the Camera class
    camera = Camera()
    # Streamlit UI
    st.title("real-Time detction")
    RTDdesc="""when a camera is able to point out different objects colour etc\nit is known as real time detecton below\nis how you will see the application of realtime detection:"""
    st.text(RTDdesc)
    st.markdown("""
        <style>
        div.stButton {text-align:center}
        </style>""", unsafe_allow_html=True)
    button_placeholder = st.empty()

    # Button to start the camera
    col1, col2, col3 = st.columns(3)
    # with col2:
        
    start_button = button_placeholder.button("Start Camera", key="start_button", type="primary")
    

    if start_button:
        button_placeholder.empty()
        frame_slot = st.empty()
        with col2:
            st.markdown(
                """ <center><h1>Face Detection</h1></center>
                

                    """,unsafe_allow_html=True
            )
        with col2:
            stop_button=st.button("stop cam")

        # Continuously capture and display video
        while True:
            frame = camera.get_frame()
            if frame is None:
                break

            labels_folder_path = "faces"
            labels = camera.load_labels_from_folder(labels_folder_path)

            frame_with_faces = camera.recognize_faces(frame, labels)
            frame_with_faces = cv2.cvtColor(frame_with_faces, cv2.COLOR_BGR2RGB)
            

            frame_slot.image(frame_with_faces, channels="RGB", use_column_width=True)

            # Check for stop button
            if stop_button:
                break

# Release the camera
camera.release_camera()

with tab2:
    # Streamlit UI
    st.title("Image Processing")
    st.write("""This application showcases the ability to detect objects using machine learning programs 
                to find and detect objects within an image""")

    # File uploader for image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    # Folder to save the uploaded image
    saved_folder = "saved_images"
    os.makedirs(saved_folder, exist_ok=True)

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        # Save the image to the specified folder
        save_path = os.path.join(saved_folder, "saved_image.jpeg")
        image.save(save_path)
        image=Image.open(save_path)
        image_placeholder = st.empty()
        image_placeholder.image(image, caption="Image Detected", use_column_width=True)
        temp_uploaded_file = uploaded_file.getvalue()

        # Button to end the task (stop displaying the image and delete it)
        end_task = st.button("End Task")
        if end_task:
            if temp_uploaded_file:
                temp_uploaded_file = None
                image_placeholder.empty()
                end_task = st.write(" ")
                st.success("Task ended")
            else:
                st.warning("File not found!!")
                end_task = False


