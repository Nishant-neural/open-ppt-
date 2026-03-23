import streamlit as st
from backend.pipeline.pipelineGen import generate_presentation
from backend.presentation.ppt import create_ppt

st.title("OpenPPT")

prompt = st.text_input("Enter topic")

if st.button("Generate"):
    result = generate_presentation(prompt)

    file = create_ppt(result)

    st.success("Presentation created!")

    with open(file, "rb") as f:
        st.download_button(
            label="Download PPT",
            data=f,
            file_name="presentation.pptx"
        )
