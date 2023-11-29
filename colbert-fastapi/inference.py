import requests

# Define the endpoint
url = "http://localhost:8001/search"

# Define your search request data
data = {
    "html": ["<p>Your HTML content here</p>", "<p>More HTML content</p>"],  # Example HTML content
    "query": "Your search query",
    "task_id": 1,
    "k": 5
}

# Make the POST request
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    print("Search Results:", response.json())
else:
    print("Error:", response.text)
