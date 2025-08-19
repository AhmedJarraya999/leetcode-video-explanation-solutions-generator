import streamlit as st
from src.explanation_generator import generate_explanation
from src.video_generator import generate_video
from src.tts_generator import text_to_speech  # assuming you have TTS
import os
from config import OUTPUT_DIR

st.title("LeetCode Video Generator")

# Input for problem link
problem_link = st.text_input("Paste LeetCode problem link:")

if st.button("Generate Video"):
    if problem_link:
        st.info("Fetching problem text...")
        
        # TODO: Fetch problem text from the link
        problem_text = "Sample problem text for testing..."  # Replace with actual fetch
        
        st.info("Generating explanation...")
        explanation = generate_explanation(problem_text)
        
        st.info("Generating narration...")
        audio_file = text_to_speech(explanation)  # TTS function you already have
        
        st.info("Generating video...")
        video_file = generate_video(problem_text, explanation, audio_file)
        
        st.success("Video generated successfully!")
        st.video(video_file)
    else:
        st.error("Please enter a problem link.")
