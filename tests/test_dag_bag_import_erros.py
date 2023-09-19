import os
import pytest
from airflow.models import DagBag


def get_import_errors():
    """
    Generate a tuple for import errors in the dag bag
    """

    dag_bag = DagBag(include_examples=False)

    def strip_path_prefix(path):
        return os.path.relpath(path, os.environ.get("AIRFLOW_HOME"))

    # prepend "(None,None)" to ensure that a test object is always created even if it's a no op.
    return [(None, None)] + [
        (strip_path_prefix(k), v.strip()) for k, v in dag_bag.import_errors.items()
    ]


@pytest.mark.parametrize(
    "rel_path,rv", get_import_errors(), ids=[x[0] for x in get_import_errors()]
)
def test_file_imports(rel_path, rv):
    """Test for import errors on a file"""
    if rel_path and rv:
        raise Exception(f"{rel_path} failed to import with message \n {rv}")


@pytest.mark.parametrize(
    "dag_id,dag,fileloc", get_dags(), ids=[x[2] for x in get_dags()]
)
def test_dag_tags(dag_id, dag, fileloc):
    """
    test if all DAGs contain a task and all tasks use the trigger_rule all_success
    """
    assert dag.tasks, f"{dag_id} in {fileloc} has no tasks"
    for task in dag.tasks:
        t_rule = task.trigger_rule
        assert (
            t_rule == "all_success"
        ), f"{task} in {dag_id} has the trigger rule {t_rule}"