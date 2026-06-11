import os
import json
import pandas as pd


def transform_flights():
    input_path = "/opt/airflow/data/bronze/flights_raw.json"
    output_path = "/opt/airflow/data/silver/flights_clean.csv"

    with open(input_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    flights = data.get("flights", [])

    registros = []

    for flight in flights:
        registros.append({
            "flight_id": flight.get("id"),
            "flight_name": flight.get("flightName"),
            "schedule_date": flight.get("scheduleDate"),
            "schedule_time": flight.get("scheduleTime"),
            "flight_direction": flight.get("flightDirection"),
            "terminal": flight.get("terminal"),
            "gate": flight.get("gate"),
            "airline_code": flight.get("prefixIATA"),
            "service_type": flight.get("serviceType"),
            "public_flight_state": ",".join(
                flight.get("publicFlightState", {}).get("flightStates", [])
            )
        })

    df = pd.DataFrame(registros)

    os.makedirs("/opt/airflow/data/silver", exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8")

    print("Transformação concluída com sucesso!")