import sys
from datetime import datetime, timedelta
from pathlib import Path

from airflow.sdk import dag, get_current_context, task

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.extract import extract
from src.load import load
from src.transform import transform


@dag(
    dag_id="xcom_gas_price",
    schedule=timedelta(minutes=1),
    start_date=datetime(2026, 6, 6),
    catchup=False,
)
def pipeline():
    @task
    def extract_func():
        ti = get_current_context()["ti"]

        raw_data = extract()

        ti.xcom_push(
            key="raw_path",
            value=raw_data,
        )

    @task
    def transform_func():
        ti = get_current_context()["ti"]

        raw_data = ti.xcom_pull(
            task_ids="extract_func",
            key="raw_data",
        )

        transformed_data = transform(raw_data)

        ti.xcom_push(
            key="transformed_path",
            value=transformed_data,
        )

    @task
    def load_func():
        ti = get_current_context()["ti"]

        state, cities = ti.xcom_pull(
            task_ids="transform_func",
            key="transformed_path",
        )

        load(state, cities)

    extract_func() >> transform_func() >> load_func()


dag = pipeline()
