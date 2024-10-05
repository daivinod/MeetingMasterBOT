# Meeting Master BOT

Meeting Master BOT is a powerful tool designed to transcribe audio files seamlessly into text using the state-of-the-art **Whisper** model.

## Key Features

- **High-Quality Transcription**: Converts audio files to accurate and readable text with ease.
- **Whisper Model Integration**: Utilizes OpenAI's advanced Whisper model to ensure high accuracy and speed.
- **Streamlit Interface**: Simple and user-friendly interface powered by Streamlit for easy accessibility.
- **GPU-Optimized Performance**: Designed to leverage CUDA for efficient processing, ensuring fast transcriptions on compatible hardware.

## Prerequisites

To run the application smoothly, ensure you have the following:

- **Python Environment**: The tool requires Python and associated libraries to be installed.
- **GPU & CUDA Support (Optional)**: For optimal performance, it is recommended to have a compatible GPU with CUDA capabilities.

## Setup & Installation

1. **Clone the Repository**: Start by cloning the project repository:
   ```bash
   git clone https://github.com/daivinod/MeetingMasterBOT
   cd https://github.com/daivinod/MeetingMasterBOT
   pip install -r requirements.txt
   streamlit run app.py --server.port=6007
 