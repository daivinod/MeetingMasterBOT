# Audio Transcription and Summarization

This project provides a tool for transcribing audio files into text using the **Whisper** model.

## Features


## Requirements

To run this project, you'll need to install the necessary Python libraries and ensure that you have a compatible GPU if you're running on CUDA.

### Install Dependencies

```bash
pip install faster-whisper transformers torch


You can use device="cpu" instead of device="cuda" if you don't have GPU support or want to run the model on your CPU. Changing the device to "cpu" will bypass the need for CUDA and CuDNN, allowing your model to run on the CPU.

Here’s how to modify the code to run on the CPU:

def transcribe_audio(audio_path, model_size="large-v2", device="cpu", compute_type="int8_float16"):

In the transcribe_audio function, the device argument is now set to "cpu". This will allow the model to run on your CPU. However, note that transcribing audio using the CPU will be slower compared to using a GPU.

Make sure to also update the compute_type to "float32" if you’re using the CPU, as int8_float16 is optimized for GPUs:

def transcribe_audio(audio_path, model_size="large-v2", device="cpu", compute_type="float32"):

After making these changes, the program should work fine on a CPU. Just be mindful of the slower processing time on larger models like "large-v2".


