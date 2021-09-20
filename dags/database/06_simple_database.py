from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

from helpers.defaults import default_args


dag = DAG(
    dag_id="06_simple_database_dag",
    start_date=datetime(2021, 1, 20, 19),
    schedule_interval=timedelta(days=1),
    default_args=default_args,
    tags=['database'],
)

task1 = PostgresOperator(
    task_id='01_simple_database_task',
    postgres_conn_id='local_docker_postgres',
    sql="sql/sql/insert.sql",
    parameters=("listing title", "listing description"),
)
