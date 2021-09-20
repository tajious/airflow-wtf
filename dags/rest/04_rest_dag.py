from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime, timedelta

from helpers.defaults import default_args


dag = DAG(
    dag_id="04_simple_rest_dag",
    start_date=datetime(2021, 1, 20, 19),
    schedule_interval=timedelta(days=1),
    default_args=default_args,
    tags=['rest'],
)

task1 = SimpleHttpOperator(
    http_conn_id='trumpet_staging_host',
    task_id='04_simple_rest',
    endpoint='/api/v5.6.0/general/static-data/version',
    method='GET',
    response_check=lambda response: response.status_code < 400,
    response_filter=lambda response: response.json(),
    dag=dag,
)
