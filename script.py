import requests


r = requests.get("http://httpbin.org/get")
print(f"Status code: {r.status_code}")

def divide(x,y):
    return x/y

