from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

# Define the DAG
dag = DAG(
    dag_id='every_30_seconds',
    description='A simple DAG that runs every 30 seconds',
    schedule_interval='*/30 * * * *',  # Every 30 seconds
    start_date=days_ago(1),  # Start date for the DAG
    catchup=False,  # Don't perform catch-up runs
    default_args={
        'owner': 'airflow',  # Owner of the DAG
        'retries': 1,  # Number of retries for each task
        'retry_delay': timedelta(seconds=10)  # Delay between retries
    }
)

# Define a simple task
start = DummyOperator(
    task_id='start',
    dag=dag
)

# Task that runs a simple Bash command
run_bash = BashOperator(
    task_id='run_bash',
    bash_command='echo "Running every 30 seconds"',
    dag=dag
)

# Define task dependencies
start >> run_bash
