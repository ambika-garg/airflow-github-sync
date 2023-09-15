from airflow.models import DagBag


def test_import_dags():
    dagbag = DagBag(dag_folder="dags", include_examples=False)
    assert not dagbag.import_errors
