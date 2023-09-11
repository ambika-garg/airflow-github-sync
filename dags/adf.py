from datetime import datetime
from airflow.models import Variable
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="demo_one", start_date=datetime(2023, 8, 15), schedule="0 0 * * *") as dag:

    # Tasks are represented as operators
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    @task()
    def airflow():
        print("airflow")

    @task()
    def gitsync():
        print("gitsync")

    # @task()
    # def printVar():
    #     foo = Variable.get("foo")
    #     print(foo)

    # Set dependencies between tasks
    hello >> airflow() >> gitsync()