import pprint
from datetime import datetime, timedelta
from typing import Dict, List

from airflow.decorators import dag, task

from helpers.defaults import default_args


@dag(default_args=default_args, start_date=datetime(2021, 1, 25, 16), tags=['taskflow', 'v2'])
def local_taskflow_etl():

    @task()
    def extract() -> List[int]:
        return [i for i in range(50)]

    @task()
    def transform(data: List[int]) -> Dict[str, int]:
        return {str(i): v for i, v in enumerate(data)}

    @task()
    def load(data: Dict[str, int]):
        print('Loading data somewhere nice')
        pprint.pprint(data)

    list_data = extract()
    dict_data = transform(list_data)
    load(dict_data)


taskflow_etl_dag = local_taskflow_etl()
