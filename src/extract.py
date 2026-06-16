import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")
url = os.getenv("url")

headers = {
    "content-type": "application/json",
    "authorization": f"apikey {api_key}",
}

params = {"state": "WA"}


def extract():
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        return data["result"]
    except requests.RequestException as e:
        print(f"Extractiong error: {e}")
        return None
