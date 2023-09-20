# from datetime import datetime
# from airflow.operators.bash import BashOperator
# from airflow.models import DAG
import pytest
from airflow.models import DagBag


@pytest.fixture()
def dagbag():
    return DagBag(dag_folder="dags")


def test_no_import_errors(dagbag):
    """
        Test Dags to contain no import errors.
    """
    assert not dagbag.import_errors


def test_expected_dags(dagbag):
    """
        Test whether expected dag Ids are present.
    """
    expected_dag_ids = ["airflow-ci-cd-tutorial"]
    for dag_id in expected_dag_ids:
        dag = dagbag.get_dag(dag_id)

        assert dag is not None
        assert dag_id == dag.dag_id


def test_requires_specific_tag(dagbag):
    """
        Test if DAGS contain one or more tags from list of approved tags only.
    """
    Expected_tags = {"ABC"}
    dagIds = dagbag.dag_ids

    for id in dagIds:
        dag = dagbag.get_dag(id)
        assert dag.tags
        if Expected_tags:
            assert not set(dag.tags) - Expected_tags


# def test_dag(dagbag):
#     """Validate a complete DAG"""
#     dagIds = dagbag.dag_ids
#     logging.info("dagIds", dagIds)
#     print(dagIds)

#     for id in dagIds:
#         dag = dagbag.get_dag(id)
#         dag.test()
