# Copyright (c) 2024 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import boto3
import aws_session_handler
import json

import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)


# get all lambda functions of a region and return a list of functions
def get_lambda_functions(region):
    logger.debug('START - get_lambda_functions(region)')
    logger.debug('region: %s', region)
    session = aws_session_handler.get_session()
    lambda_client = session.client('lambda', region_name=region)
    functions = lambda_client.list_functions()
    functions_list = []
    for lambdafunction in functions['Functions']:
        functions_list.append(lambdafunction)
    return functions_list


# get information about a lambda function
def get_lambda_function(region, function_name):
    logger.debug('START - get_lambda_function(region, function_name)')
    logger.debug('region: %s', region)
    logger.debug('function_name: %s', function_name)
    session = aws_session_handler.get_session()
    lambda_client = session.client('lambda', region_name=region)
    lambdafunction = lambda_client.get_function(FunctionName=function_name)
    return lambdafunction


# invoke a lambda function
def invoke_lambda_function(region, function_name, payload):
    logger.debug('START - invoke_lambda_function(region, function_name, payload)')
    logger.debug('region: %s', region)
    logger.debug('function_name: %s', function_name)
    logger.debug('payload: %s', payload)
    session = aws_session_handler.get_session()
    lambda_client = session.client('lambda', region_name=region)
    response = lambda_client.invoke(FunctionName=function_name, Payload=payload)
    return json.dumps(response, indent=2, default=str)
