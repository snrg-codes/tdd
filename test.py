import requests

url = "http://192.168.100.65:5000/login"

payload = {
    "username" : "admin",
    "password" : "1234"
}

response = requests.post(url, json=payload)
assert response.status_code == 200
assert response.text is not None



