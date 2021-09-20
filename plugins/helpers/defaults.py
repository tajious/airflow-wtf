from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['example@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
}
