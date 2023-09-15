# import os
# import mock
# import pytest
# from airflow.models import DagBag

# @pytest.fixture(scope='module')#scope increased so that dag loading happens once
# @mock.patch.dict(os.environ, {"key":"value"})#mocking os vars 
# def dag_bag():
#   # Create an instance of the `DagBag` class
#   dagbag = DagBag(dag_folder='dags', include_examples=False)
#   # Return the DagBag instance
#   return dagbag

# def test_dags_load_with_no_errors(dag_bag):
#     print(dag_bag.dags)
#     assert dag_bag.dags is not None
#     assert len(dag_bag.import_errors) == 0
