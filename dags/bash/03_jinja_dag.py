from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

from helpers.defaults import default_args


dag = DAG(
    dag_id="03_jinja_template_tag",
    start_date=datetime(2021, 1, 20, 19),
    schedule_interval=timedelta(days=1),
    default_args=default_args,
    tags=['bash'],
)

command = """
{% for i in params.names %}
    echo "random item is: {{ i }}"
{% endfor %}
"""

some_list = ["Jack", "MySQL", "Tabbat", "Habibi", "Smith", "Ruby"]

task1 = BashOperator(task_id='templated_bash', bash_command=command, params={'names': some_list}, dag=dag)
