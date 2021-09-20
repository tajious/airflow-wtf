from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

from helpers.defaults import default_args


dag = DAG(
    dag_id="02_complex_bash_dag",
    start_date=datetime(2021, 1, 20, 19),
    schedule_interval=timedelta(days=1),
    default_args=default_args,
    tags=['bash'],
)


task1 = BashOperator(task_id='01_bash_complex', bash_command='echo "Hello"', dag=dag)
task2 = BashOperator(task_id='02_bash_complex', bash_command='echo `date`', dag=dag)
task3 = BashOperator(task_id='03_bash_complex', bash_command='echo "I depend on printing date"', dag=dag)
task4 = BashOperator(task_id='04_bash_complex', bash_command='echo "I also depend on printing date"', dag=dag)
task5 = BashOperator(task_id='05_bash_complex', bash_command='echo "I should be run last, goodbye"', dag=dag)
task6 = BashOperator(task_id='06_bash_complex', bash_command='echo "I don\'t depend on anything"', dag=dag)

task1 >> task2 >> [task3, task4] >> task5
