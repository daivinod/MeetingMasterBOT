import requests
import json

def preprocess_text(text):
    lines = text.split('\n')
    processed_lines = [line for line in lines if not line.strip().startswith(tuple('0123456789')) and line.strip() != '']
    return '\n'.join(processed_lines)

def split_text(text, word_limit=1300):
    """
    Splits a given text into chunks of a specific size.

    Parameters:
    text (str): The text to be split.
    word_limit (int): The maximum size of each chunk.

    Returns:
    list: The list of chunks.
    """
    words = text.split()
    num_parts = len(words) // word_limit + 1
    return [' '.join(words[i * word_limit: (i + 1) * word_limit]) for i in range(num_parts)]

def load_prompt(filename="./prompt.json"):
    """
    Loads a prompt from a JSON file.

    Parameters:
    filename (str): The name of the JSON file.

    Returns:
    list: The loaded prompt.
    """
    with open(filename, "r") as f:
        return json.load(f)

def get_summary(transcript):
    # Preprocess the transcript if necessary
    chunks = split_text(transcript)
    summary_list = []
    
    # Load the prompt
    prompt = load_prompt()

    # Process each chunk
    for i, chunk in enumerate(chunks, start=1):
        prompt[-2]["content"] = chunk
        url = "http://llm.neorains.com/api/chat"
        payload = {
            "model": "llama3.1",
            "messages": prompt, 
            "stream": False,
            "options": {
                "temperature": 0
            }
        }
        payload_json = json.dumps(payload)
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=payload_json, headers=headers)
        
        if response.status_code == 200:
            response_json = response.json()
            summary = response_json['message']['content']
            summary_list.append(summary)
        else:
            print(f"Error: Received status code {response.status_code}")
            break

    # Combine all summaries into one text
    combined_summary = '\n'.join(summary_list)
    
    # Generate a final cohesive summary of the combined text
    prompt[-2]["content"] = combined_summary
    payload = {
        "model": "llama3.1",
        "messages": prompt, 
        "stream": False,
        "options": {
            "temperature": 0
        }
    }
    payload_json = json.dumps(payload)
    response = requests.post(url, data=payload_json, headers=headers)
    
    if response.status_code == 200:
        response_json = response.json()
        final_summary = response_json['message']['content']
    else:
        print(f"Error during final consolidation: Received status code {response.status_code}")
        final_summary = combined_summary  # Fall back to the combined summaries

    return final_summary


