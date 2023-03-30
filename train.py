import requests

capture_title = "My Capture Title Here"
auth_headers = {'Authorization': 'luma-api-key=ec167066-0fe8-46da-8aab-a372f2bfccab-9be191d-ff20-4f1e-a439-bc42cfe19e93'}

response = requests.post("https://webapp.engineeringlumalabs.com/api/v2/capture",
                         headers=auth_headers,
                         data={'title': capture_title})
capture_data = response.json()
upload_url = capture_data['signedUrls']['source']
slug = capture_data['capture']['slug']

print(capture_data)
print("Upload URL:", upload_url)
print("Capture slug:", slug)