from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator

from helpers.defaults import default_args


dag = DAG(
    dag_id="05_complex_rest_dag",
    start_date=datetime(2021, 1, 20, 19),
    schedule_interval=timedelta(days=1),
    default_args=default_args,
    tags=['rest'],
)

task1 = SimpleHttpOperator(
    http_conn_id='trumpet_staging_host',
    task_id='01_complex_rest',
    endpoint='/api/v5.6.0/general/static-data/vson',
    method='GET',
    response_check=lambda response: False,
    response_filter=lambda response: response.json(),
    dag=dag,
)


def print_xcom_results(**kwargs):
    ti = kwargs['ti']
    task1_result = ti.xcom_pull(task_ids='01_complex_rest')
    print(task1_result)


task2 = PythonOperator(task_id='02_complex_rest_bash', python_callable=print_xcom_results, retries=4, dag=dag)

task1 >> task2
