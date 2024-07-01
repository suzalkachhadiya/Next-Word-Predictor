import streamlit as st
import os
from NWPproject.constants import *

st.set_page_config(
    page_title="NWP training",
    page_icon="⌨️",
    layout="wide"
)

st.header("Model Training", divider="rainbow")

st.write("Upload a file containing texts.")
# Create the upload folder if it doesn't exist
if not os.path.exists(SAVED_FILE_PATH):
    os.makedirs(SAVED_FILE_PATH)

uploaded_file = st.file_uploader("Choose a text file", type="txt")

if uploaded_file is not None:
        # Display the original filename
        st.write(f"Uploaded file: {uploaded_file.name}")

        # Read and display the content of the file
        content = uploaded_file.getvalue().decode("utf-8")
        st.text_area("Please check your File Content here before uploading for the training", content, height=200)

        if st.button("Save File & Train Model"):
            # Full path for saving the file
            save_path = os.path.join(SAVED_FILE_PATH, uploaded_file.name)

            # Save the text file
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # st.success(f"Text file saved as: {save_path}")

# st.write("""
#     Initiate the model training process by clicking the 'Start' button. 
#     Please be aware that the duration of this training may vary, depending on the performance specifications of your device. 
    
#     Thank you for your patience..
# """)