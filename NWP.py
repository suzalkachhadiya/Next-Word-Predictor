import streamlit as st

st.set_page_config(
    page_title="NWP", 
    page_icon="⌨️",
    layout="wide"
)
st.title("Next Word _ _ :blue[Predictor] _ _")

st.write("\n")

st.header("Improving typing speed",divider="rainbow")
st.write("Our next word predictor is designed to significantly boost your typing speed. By analyzing the context of your current text, it suggests the most likely next words, allowing you to complete sentences faster. This tool learns from your writing style over time, making increasingly accurate predictions. With practice, you'll find yourself relying on these suggestions more frequently, reducing the number of keystrokes needed and ultimately increasing your overall typing speed and efficiency.")

st.write("\n")

st.header("How it works?", divider="rainbow")
st.write("Our next word predictor operates by learning from your text input. Start by uploading a file containing sample text that reflects your writing style or the type of content you typically work with. The model analyzes this text to understand patterns, word associations, and common phrases. As you type, the predictor draws upon this learned knowledge to suggest the most probable next words based on the context of what you've already written. This dynamic process adapts to your unique writing style, offering increasingly accurate predictions over time and enhancing your typing efficiency.")

st.write("\n")

st.header("What is the approach behind it?", divider="rainbow")
st.write("Sentences of the data will get converted into array by numbering a words of it. For predicting a word it'll be considered as multiclass classification problem. Model will be training on the Long Short Term Memomry (LSTM).")

st.write("\n")

st.markdown("---")
st.subheader("Let's Connect")
st.write("LinkedIn: https://www.linkedin.com/in/suzal-kachhadiya-149498237/")
st.write("GitHub: https://github.com/suzalkachhadiya")
st.write("Email: suzalkachhadiya@gmail.com")
st.write("Phone: +91 8488855887")

# Create a dictionary of page names to module paths
# pages = {
#     "Model Train": "pages.quality_prediction.py", 
#     "Quality Prediction": "pages.model_training.py"
# }

