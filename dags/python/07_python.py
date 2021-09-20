from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from helpers.defaults import default_args


dag = DAG(
    dag_id="08_python_dag",
    start_date=datetime(2021, 1, 20, 19),
    schedule_interval=timedelta(days=1),
    default_args=default_args,
    tags=['python'],
)


def generate_some_numbers(**kwargs):
    return [i for i in range(50)]


def multiply_those_numbers(**kwargs):
    ti = kwargs['ti']
    some_numbers = ti.xcom_pull(task_ids=['01_python_task'])
    multiplied_numbers = [i * 2 for i in some_numbers]
    return multiplied_numbers


task1 = PythonOperator(
    task_id='01_python_task',
    python_callable=generate_some_numbers,
    dag=dag,
)

task2 = PythonOperator(
    task_id='02_python_task',
    python_callable=multiply_those_numbers,
    dag=dag,
)

task1 >> task2
