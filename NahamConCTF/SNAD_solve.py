import requests
import json

URL = "http://challenge.nahamcon.com:32589/api/verify-ctf-solution"

# Danh sách các hạt cát đúng vị trí và màu sắc (theo hue)
particle_data = [
    {"x": 367, "y": 238, "colorHue": 0},
    {"x": 412, "y": 293, "colorHue": 40},
    {"x": 291, "y": 314, "colorHue": 60},
    {"x": 392, "y": 362, "colorHue": 120},
    {"x": 454, "y": 319, "colorHue": 240},
    {"x": 349, "y": 252, "colorHue": 280},
    {"x": 433, "y": 301, "colorHue": 320}
]

headers = {
    "Content-Type": "application/json"
}

payload = {
    "particleData": particle_data
}

response = requests.post(URL, headers=headers, data=json.dumps(payload))

try:
    data = response.json()
    if data.get("success"):
        print("[✅] Flag:", data.get("flag"))
    else:
        print("[❌] Failed:", data.get("message"))
except Exception as e:
    print("[⚠️] Error parsing response:", str(e))
    print("Raw response:", response.text)

