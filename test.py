import requests


raw_url = 'https://acbf-86-10-113-94.ngrok-free.app/'
req_url = raw_url + "/summarize"
path = r"C:\Users\bahar\Synopsis AI\discharge-summaries\Example Training\2 (Single File Format)\input"

text = open(path, "r").read()


data = {
    'inputText': text  # Replace with your test input
}
response = requests.post(req_url, json=data)

# Print the result
print(response.json())
