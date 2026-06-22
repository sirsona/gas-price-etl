import sys
from pathlib import Path

from airflow.sdk import dag, task

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.extract import extract
from src.load import load
from src.transform import transform


@dag(dag_id="auto_xcom_gas_price")
def pipeline():
    @task
    def extract_task():
        return extract()

    @task
    def transform_task(data):
        return transform(data)

    @task
    def load_task(data):
        state, cities = data
        load(state, cities)

    load_task(transform_task(extract_task()))


dag = pipeline()
