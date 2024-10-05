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
   cd MeetingMasterBOT
   pip install -r requirements.txt
   streamlit run app.py --server.port=6007
   ```

## Demo

Check out the live demo [here](https://mmb.neorains.com).

## Summary Generation

The `Meeting Master BOT` also includes functionality to generate summaries from transcribed text using the `get_summary` function in [`summary.py`](summary.py).

### Usage

The `get_summary` function processes a transcript and generates a cohesive summary. It splits the transcript into chunks, processes each chunk using an external API, and then combines the results into a final summary.

### Example

Here is an example of how to use the `get_summary` function:

```python
from summary import get_summary

transcript = "Your transcribed text here."
summary = get_summary(transcript)
print(summary)
```

### Function Details

- **Input**: A string `transcript` containing the transcribed text.
- **Output**: A string containing the final summary of the transcript.

The function works as follows:
1. Splits the transcript into manageable chunks.
2. Loads a predefined prompt from a file.
3. Sends each chunk to an external API for processing.
4. Combines the individual summaries into a single text.
5. Sends the combined text to the API for final consolidation.
6. Returns the final summary.

For more details, refer to the implementation in [`summary.py`](summary.py).