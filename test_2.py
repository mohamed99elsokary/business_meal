import json

import requests

url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json",
}

conversation_history = []


while True:
    prompt = input("input: ")
    conversation_history.append(prompt)
    full_prompt = "\n".join(conversation_history)
    data = {
        "model": "codellama",
        "stream": False,
        "prompt": full_prompt,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        conversation_history.append(actual_response)
        print("\n")
        print("output: ", actual_response)
        print("\n")
    else:
        print("Error:", response.status_code, response.text)
        print(None)
