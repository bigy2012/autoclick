import requests

# Define the API URL you want to request
api_url = "https://graph.facebook.com/oauth/access_token?client_id=644133117609342&client_secret=1a5654a6a655e67379a2e43881a909d7&grant_type=client_credentials"

# Make a GET request
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Now, you can work with the data as needed
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")



