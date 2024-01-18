import streamlit as st
from open_camera import Camera
import cv2
from PIL import Image
import os
st.set_page_config(
    page_title="V-sigt",
	page_icon="v-sight.jpg",
	layout="wide",
    initial_sidebar_state="expanded",
    
    
)


tab1, tab2, tab3, tab4 = st.tabs(["realtime detection","image detection","games with cv","try"])

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

	# Button to start the camera
	col1, col2, col3=st.columns(3)
	with col2:
		start_button = st.button("start camera",key="start_button",type="primary")
		


	
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = None

	if start_button:
		start_button = None
		
		
		out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
		frame_slot = st.empty()
		with col2:
			st.subheader(":blue[Realtime]:red[Detection]")
		with col3:
			stop_button = st.button("Stop Camera",key="stop_button")

		# Continuously capture and display video
		while True:
			frame = camera.get_frame()
			frame = cv2.flip(frame, 1)

			# Convert frame to RGB for writing to video file
			rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

			# Write the frame to the video file
			if out is not None:
				out.write(rgb_frame)
			
			frame_slot.image(frame, channels="BGR", use_column_width=True)
			
			# Check for stop button
			if stop_button:
				break

	# Release the video writer and camera
	if out is not None:
		out.release()
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
		
		end_task =st.button("End Task")
		#st.session_state()

		if end_task:
			if temp_uploaded_file:
				temp_uploaded_file=None
				image_placeholder.empty()
				end_task=st.write(" ")
				st.success("task ended")
			else:
				st.warning("File not found!!")
				end_task=False
						
			
with tab3:
		
	with st.container():
		st.header("oops this part is currently under construction")
	col1, col2, col3=st.columns(3,gap="medium")
	with col2:
		st.header(":no_entry::no_entry::no_entry::no_entry:")

#with tab4:
	

		