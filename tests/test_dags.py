# from datetime import datetime
# from airflow.operators.bash import BashOperator
# from airflow.models import DAG
import pytest
from airflow.models import DagBag


@pytest.fixture()
def dagbag():
    return DagBag(dag_folder="dags")


def test_dag(dagbag):
    """Validate a complete DAG"""
    # with DAG(dag_id="demo_one", start_date=datetime(2023, 8, 15), schedule="0 0 * * *") as dag:

    #     # Tasks are represented as operators
    #     hello = BashOperator(task_id="hello", bash_command="echo hello")

    #     version = BashOperator(
    #         task_id="Check_python_version", bash_command="python --version")

    #     # Set dependencies between tasks
    #     hello >> version
    #     dag.test()
    dagIds = dagbag.dag_ids
    print(dagIds)
