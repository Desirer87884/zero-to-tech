import requests

resp = requests.get("http://localhost:8000/api/profile")
print(resp.json())
