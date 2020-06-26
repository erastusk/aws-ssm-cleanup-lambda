#!/usr/bin/env python3
"""
Lambda function for deleting "orphaned" Parameter store
.. pipeline parameters
"""

from datetime import datetime
from botocore.exceptions import ClientError, ParamValidationError
import boto3

SSM = boto3.client('ssm')
def describe_parameters(params):
    """
    Describe parameters in SSM by parameter filters.
    Initially there were over 800 orphaned parameters so pagination is required.
    Might not be the case after the first bulk delete
    """
    param_date = {}
    try:
        for param_filter in params:
            paginator = SSM.get_paginator('describe_parameters')
            params = paginator.paginate(
                ParameterFilters=[
                    {
                        'Key': 'Name',
                        'Option': 'Contains',
                        'Values': [
                            param_filter
                        ]
                    }
                ],
            )
            for resp_dict in params:
                if resp_dict['Parameters']:
                    for param_name in resp_dict['Parameters']:
                        param_date[param_name['Name']
                                   ] = param_name['LastModifiedDate']
        return param_date
    except ClientError as cleerror:
        raise cleerror
    except ParamValidationError as paramerror:
        raise paramerror


def modify_parameter_dates(params, age):
    """
    Parse and keep parameters with a creation exceeding specified age for deletion,
    discard the rest.
    Parameters retrieved date and time values are "aware", meaning they include
    a timezone.Datetime module is being used to add timezone to datetime.now.
    datetime.datetime(2020, 6, 10, 14, 44, 37, 249000, tzinfo=tzlocal())
    If Age = 0, delete all parameters.
    """
    if age == 0:
        return [key for key, val in params.items()]
    time_delta_list = [key for key, val in params.items() if (
        (datetime.now(val.tzinfo)) - val).days > age]
    if time_delta_list:
        return time_delta_list
    return None


def delete_parameters(params):
    """
    ssm delete_parameter command has a limit of 10.Edited to
    send delete in batches of 10.
    Member must have length less than or equal to 10.", 'Code': 'ValidationException'
    """
    try:
        response = SSM.delete_parameters(
            Names=params
        )
        if response['InvalidParameters']:
            return "Following SSM parameters do not exist{}".format(
                response['InvalidParameters'])
        return "Following SSM parameters were deleted{}".format(
            response['DeletedParameters'])
    except ClientError as cleerror:
        raise cleerror
    except ParamValidationError as paramerror:
        raise paramerror
