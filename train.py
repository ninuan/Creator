import requests
import os

#获得最近获得的文件
def get_most_recently_uploaded_file(directory):
    # Get a list of files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    if not files:
        return None

    # Find the most recently uploaded file by comparing modification times
    most_recent_file = max(files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
    return most_recent_file

def train():
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

  filename = get_most_recently_uploaded_file('./models')
  with open("filename", "rb") as f:
      payload = f.read()
  
  # upload_url from step (1)
  response = requests.put(upload_url, headers={'Content-Type': 'text/plain'}, data=payload)
  
  # Note: the payload should be bytes containing the file contents (as shown above)!
  # A common pitfall is uploading the file name as the file contents
  
  print(response.text)
  
  # slug from Capture step
  
  auth_headers = {'Authorization': 'luma-api-key=ec167066-0fe8-46da-8aab-a372f2bfccab-9be191d-ff20-4f1e-a439-bc42cfe19e93'}
  response = requests.post(f"https://webapp.engineeringlumalabs.com/api/v2/capture/{slug}",
                           headers=auth_headers)
  
  print(response.text)
  
  # slug from Capture step
  
  auth_headers = {'Authorization': 'luma-api-key=ec167066-0fe8-46da-8aab-a372f2bfccab-9be191d-ff20-4f1e-a439-bc42cfe19e93'}
  response = requests.get(f"https://webapp.engineeringlumalabs.com/api/v2/capture/{slug}",
                          headers=auth_headers)
  
  print(response.text)