#importing necessary libraries
import streamlit as st
from io import BytesIO
from main import text_to_speech

#streamlit title
st.title('Text to Speech with Amazon Polly')
st.write('Enter text below and click on "Submit" to convert text to speech.')

#place to enter text
input_text = st.text_area("Enter text")

#if submit button is clicked
if st.button('Submit'):
    if input_text:
        audio_bytes = text_to_speech(input_text)
        
        # Display audio player
        st.audio(audio_bytes, format='audio/mp3', start_time=0)

# further instructions
st.markdown('### Instructions:')
st.write("1. Enter text into the text area above.")
st.write("2. Click on 'Submit' to convert the text to speech.")