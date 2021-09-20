INSERT INTO listings (title, description) VALUES
{% for i in ti.xcom_pull(task_ids='some_task_id') %}
    (i['title'], i['description']),
{% endfor %}
