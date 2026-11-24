import requests
import subprocess

try:
    response = requests.get("http://localhost:5000/health")

    if response.text == "UP":
        print("Application Running Fine")

except:
    print("Application Down")
    print("Restarting Application...")

    subprocess.Popen(["python", "app.py"])