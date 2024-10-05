import streamlit as st
import requests

from summary import get_summary

# Define the URL of your Flask API
API_URL = "http://api.whisper.neorains.com/transcribe"

# Set up the layout
st.set_page_config(layout="wide")  # Enables the wide layout in Streamlit

st.title("Meeting Master BOT")
# Sidebar for file upload and transcribe button
with st.sidebar:
    st.header("Upload Audio")

    # File uploader widget in the sidebar
    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

    # Transcribe button in the sidebar
    if st.button("Start") and audio_file is not None:
        # Send the audio file to the Flask API
        files = {"audio": audio_file}
        
        with st.spinner("Transcribing..."):
            response = requests.post(API_URL, files=files)

        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()

            # Store transcription in session state
            st.session_state['transcription'] = data
        else:
            st.error("Error: Could not transcribe the audio file.")
    elif audio_file is None:
        st.warning("Please upload an audio file.")

# Main content area (Right below the header)
if audio_file is not None:
    # Play the uploaded audio file
    st.subheader("Audio Playback")
    st.audio(audio_file, format="audio/wav")

# Display transcription result
if 'transcription' in st.session_state:
    data = st.session_state['transcription']
    
    st.subheader("Transcription Result")
    # Collect all segments in a single string inside the scrollable div
    segments_html = """
        <div style="height: 200px; overflow-y: scroll; padding: 10px; border: 1px solid #ccc;">
    """

    for segment in data['segments']:
        segments_html += f"<p>[{segment['start']:.2f}s -> {segment['end']:.2f}s]: {segment['text']}</p>"

    # Close the div
    segments_html += "</div>"

    # Display the full HTML structure at once
    st.markdown(segments_html, unsafe_allow_html=True)
    st.session_state['summary'] = data['transcription']

if 'summary' in st.session_state:
    data = st.session_state['summary']
    st.subheader("Meeting Summary")
    summary_html = """
        <div style="height: 200px; overflow-y: scroll; padding: 10px; border: 1px solid #ccc;">
    """
    with st.spinner("Summarizing..."):
        summary_html= get_summary(data)

    # Close the div
    summary_html += "</div>"

    # Display the full HTML structure at once
    with st.spinner("Done!"):
        st.markdown(summary_html, unsafe_allow_html=True)