from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.executors.debug_executor import DebugExecutor
from airflow.utils.state import State
from airflow.models import DAG, DagRun, TaskInstance


def test_dag():
    """Validate a complete DAG"""
    with DAG(dag_id="demo_one", start_date=datetime(2023, 8, 15), schedule="0 0 * * *") as dag:

        # Tasks are represented as operators
        hello = BashOperator(task_id="hello", bash_command="echo hello")

        version = BashOperator(
            task_id="Check_python_version", bash_command="python --version")

        # Set dependencies between tasks
        hello >> version
        dag.test()

        # dag.clear()
        # dag.run(executor=DebugExecutor(),
        #         start_date=dag.start_date, end_date=dag.start_date)

        # # Validate DAG run was successful
        # dagruns = DagRun.find(dag_id=dag.dag_id, execution_date=dag.start_date)
        # assert len(dagruns) == 1
        # assert dagruns[0].state == State.SUCCESS

        # # Validate task states
        # expected_task_states = {
        #     hello: State.SUCCESS,
        #     version: State.SUCCESS,
        # }
        # for task, expected_state in expected_task_states.items():
        #     ti = TaskInstance(task, dag.start_date)
        #     ti.refresh_from_db()
        #     assert ti.state == expected_state
