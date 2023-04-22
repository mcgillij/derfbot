import requests

# Define the URL and JSON payload
url = 'http://localhost:8000/v1/chat/completions'
payload = {
    "model": "vicuna-7b-v1.1",
    "messages": [
        {"role": "user", "content": "Can you tell me a Kobold joke?"}
    ]
}

# Set the headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request with JSON payload and headers
response = requests.post(url, json=payload, headers=headers)

# Check the response status code and content
if response.status_code == 200:
    # Success
    response_json = response.json()
    print("Response:")
    print(response_json)
else:
    # Failure
    print(f"Failed with status code {response.status_code}: {response.text}")
