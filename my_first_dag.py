from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators import BashOperator

dag = DAG('my_first_dag', description='Testing dag',
          schedule_interval='0 12 * * *',
          start_date=datetime(2018, 12, 3), catchup=False)

test_operation = BashOperator(task_id='my_first_dag',bash_command="ifconfig -a",dag=dag)
test2_operation = BashOperator(task_id='my_second_dag',bash_command="ifconfig -a",dag=dag)
test3_operation = BashOperator(task_id='my_third_dag',bash_command="ifconfig -a",dag=dag)
test4_operation = BashOperator(task_id='my_fourth_dag',bash_command="ifconfig -a",dag=dag)
test5_operation = BashOperator(task_id='my_fifth_dag',bash_command="ifconfig -a",dag=dag)
test6_operation = BashOperator(task_id='my_sixth_dag',bash_command="ifconfig -a",dag=dag)
test7_operation = BashOperator(task_id='my_seventh_dag',bash_command="ifconfig -a",dag=dag)
test8_operation = BashOperator(task_id='my_eigth_dag',bash_command="ifconfig -a",dag=dag)
test9_operation = BashOperator(task_id='my_ninth_dag',bash_command="ifconfig -a",dag=dag)