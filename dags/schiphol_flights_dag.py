from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

import sys
import os

sys.path.append("/opt/airflow/src")

from extract import extract_flights
from transform import transform_flights
from load import load_gold

with DAG(
    dag_id="schiphol_flights_dag",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["schiphol", "mvp"],
) as dag:

    start = PythonOperator(
        task_id="start",
        python_callable=lambda: None
    )

    extract = PythonOperator(
    task_id="extrair_voos",
    python_callable=extract_flights
    )

    transform = PythonOperator(
    task_id="transformar_voos",
    python_callable=transform_flights
    )

    load = PythonOperator(
    task_id="carregar_ouro",
    python_callable=load_gold
    )

    end = PythonOperator(
    task_id="fim",
    python_callable=lambda: print("Pipeline finalizado")
    ) 

    start >> extract >> transform >> load >> end