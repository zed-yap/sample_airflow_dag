from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators import BashOperator

dag = DAG('my_first_dag', description='Testing dag',
          schedule_interval='0 12 * * *',
          start_date=datetime(2018, 12, 3), catchup=False)

test_operation = BashOperator(task_id='my_first_dag',bash_command="ifconfig -a",dag=dag)
test2_operation = BashOperator(task_id='my_second_dag',bash_command="ifconfig -a",dag=dag)
