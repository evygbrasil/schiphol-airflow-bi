import os
import json
import requests
from dotenv import load_dotenv

load_dotenv("/opt/airflow/.env")


def extract_flights():
    app_id = os.getenv("SCHIPHOL_APP_ID")
    app_key = os.getenv("SCHIPHOL_APP_KEY")

    url = "https://api.schiphol.nl/public-flights/flights"

    headers = {
        "Accept": "application/json",
        "app_id": app_id,
        "app_key": app_key,
        "ResourceVersion": "v4"
    }

    params = {
        "includedelays": "false",
        "page": 0,
        "sort": "+scheduleTime"
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()

    os.makedirs("/opt/airflow/data/bronze", exist_ok=True)

    with open("/opt/airflow/data/bronze/flights_raw.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Extração concluída com sucesso!")