from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

from helpers.defaults import default_args


dag = DAG(
    dag_id="01_simple_bash_dag",
    start_date=datetime(2020, 11, 10, 17),
    schedule_interval=timedelta(days=1),
    default_args=default_args,
    tags=['bash'],
)

task1 = BashOperator(task_id='first_bash_task', bash_command='echo "Hello Sheypoor"', dag=dag)
task2 = BashOperator(task_id='second_bash_task', bash_command='echo "How you be doin\'?"', dag=dag)
