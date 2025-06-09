import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")

BASE_URL = "https://v6.exchangerate-api.com/v6"

def get_exchange_rate(base_currency, target_currency):
    url = f"{BASE_URL}/{API_KEY}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise Exception(f"API call failed: {data}")
    
    return data['conversion_rate']
