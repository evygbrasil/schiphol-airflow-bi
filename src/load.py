import os
import pandas as pd


def load_gold():
    input_path = "/opt/airflow/data/silver/flights_clean.csv"
    output_path = "/opt/airflow/data/gold/flights_analytics.csv"

    df = pd.read_csv(input_path)

    df["schedule_datetime"] = pd.to_datetime(
        df["schedule_date"] + " " + df["schedule_time"],
        errors="coerce"
    )

    df["hour"] = df["schedule_datetime"].dt.hour

    os.makedirs("/opt/airflow/data/gold", exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8")

    print("Carga Gold concluída com sucesso!")