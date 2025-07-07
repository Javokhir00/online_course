import requests

response = requests.post(

  "http://127.0.0.1:8000/course/api/login/",
    data = None,
  json={
        "password": "123Qwe!@#",
        "username": "javohir",
       }
)


print("Status code:", response.status_code)
print("Response text:", response.text)


try:
    data = response.json()
    print("JSON response:", data)
except Exception as e:
    print("Failed to parse JSON:", e)