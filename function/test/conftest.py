import pytest
from test_delete_parameters import describe_parameters

params = ["PACKAGE-NAME"]
@pytest.fixture()
def describe_params_fixture():
    return describe_parameters(params)
