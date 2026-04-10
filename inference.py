import requests

BASE_URL = "http://localhost:7860"

# test reset
res = requests.post(f"{BASE_URL}/reset")
print("Reset:", res.json())

# test step
res = requests.post(f"{BASE_URL}/step", json={"action": "spam"})
print("Step:", res.json())
