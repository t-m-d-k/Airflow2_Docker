from airflow import DAG
from datetime import datetime
from random import randint
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator


def _choose_model(ti):
    accuracies = ti.xcom_pull(task_ids =['Model_A','Model_B','Model_C'])
    best_accuracy = max(accuracies)
    if best_accurasy > 8 :
        return 'accurate'
    return 'innaccurate'

def _training_model():
    return randint(1,10)
with DAG("my_dag",start_date = datetime(2021,1,1), schedule_interval="@daily", catchup = False) as dag:

    Model_A = PythonOperator(task_id = "Model_A",
                            python_callable= _training_model)

    Model_B = PythonOperator(task_id = "Model_B",
                            python_callable= _training_model)

    Model_C = PythonOperator(task_id = "Model_C",
                            python_callable= _training_model)

    choose_best_model = BranchPythonOperator(task_id="choose_model",
                                            python_callable= _choose_model)
    
    
    accurate = BashOperator( task_id = "accurate" , bash_command = "echo 'accurate'")
    inaccurate = BashOperator( task_id = "inaccurate" , bash_command = "echo 'inaccurate'")

    [Model_A, Model_B, Model_C] >> choose_best_model >> [accurate, inaccurate]
