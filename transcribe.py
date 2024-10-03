import os
import streamlit as st
from faster_whisper import WhisperModel
from transformers import BartTokenizer, BartForConditionalGeneration
import torch

# Create folders if they don't exist
if not os.path.exists("uploads"):
    os.makedirs("uploads")

if not os.path.exists("transcriptions"):
    os.makedirs("transcriptions")


def transcribe_audio(audio_path, model_size="large-v2", device="cuda", compute_type="int8_float16"):
    # Initialize the Whisper model
    model = WhisperModel(model_size, device=device, compute_type=compute_type)

    # Transcribe the audio file
    segments, info = model.transcribe(audio_path, beam_size=5)

    # Print the detected language and its confidence level
    st.write(f"Detected language: {info.language} (Probability: {info.language_probability})")

    full_transcription = ''
    for segment in segments:
        full_transcription += "[%.2fs -> %.2fs] %s\n" % (segment.start, segment.end, segment.text)

    return full_transcription


def save_transcription(transcription, file_path):
    with open(file_path, 'w') as file:
        file.write(transcription)


def main():
    st.title("Audio Transcription App")
    
    # File upload UI
    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
    
    if uploaded_file is not None:
        audio_path = os.path.join("uploads", uploaded_file.name)
        
        # Save the uploaded audio file
        with open(audio_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        
        # Select device for transcription (CPU or GPU)
        device_option = st.radio("Select device to use for transcription", ("CPU", "GPU"))
        # Set compute type based on the selected device
        if device_option == "CPU":
            device = "cpu"
            compute_type = "float32"  # CPU needs float32
        else:
            device = "cuda"
            compute_type = "int8_float16"  # GPU optimized compute type
        
        # Button to start transcription
        if st.button("Transcribe Audio"):
            st.write("Starting transcription...")
            try:
                # Transcribe the audio
                transcription = transcribe_audio(audio_path, device=device, compute_type=compute_type)
                
                # Save the transcription
                transcription_path = os.path.join("transcriptions", f"{uploaded_file.name}.txt")
                save_transcription(transcription, transcription_path)
                
                st.success("Transcription completed!")
                st.write("Transcription:")
                st.text(transcription)
                
            except Exception as e:
                st.error(f"Error during transcription: {str(e)}")

if __name__ == "__main__":
    main()
