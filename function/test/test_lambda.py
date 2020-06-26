""" Test module - Pytest """
import pytest
from botocore.exceptions import ParamValidationError
from test_delete_parameters import describe_parameters, modify_parameter_dates, delete_parameters
from lambda_test import lambda_handler

# Main function testing, lambda.py

def test_check_params_variable():
    """ Return None, if param_filters variable empty """
    #actual = lambda_handler()
    assert lambda_handler is None


# describe_parameter function testing

def test_describe_test_param_exist(describe_params_fixture):
    """Query a known existing parameter in parameter store"""
    actual = describe_params_fixture
    param_key = [key for key, value in actual.items()][0]
    assert "PACKAGE-NAME" in param_key


def test_describe_params_paramvalidation_error():
    """
    Test for empty param query list -- this should throw a param
    validation error
    """
    params = [""]
    with pytest.raises(ParamValidationError) as errinfo:
        describe_parameters(params)
    assert "Parameter validation" in str(errinfo.value)

# modify_parameter_dates function testing

def test_if_age_zero_test(describe_params_fixture):
    """ If age is 0, return parameter keys passed in """
    params = describe_params_fixture
    params_key = [key for key, value in params.items()][0]
    actual = modify_parameter_dates(params, 0)
    assert params_key == actual[0]

def test_return_none_with_none_to_delete(describe_params_fixture):
    """ If none greater than age return none """
    params = describe_params_fixture
    actual = modify_parameter_dates(params, 20)
    assert actual is None

# delete_parameters function testing

def test_describe_params_paramvalidation_error_del_func():
    """
    Test for empty delete list -- this should throw a param
    validation error
    """
    params = [""]
    with pytest.raises(ParamValidationError) as errinfo:
        delete_parameters(params)
    assert "Parameter validation" in str(errinfo.value)
