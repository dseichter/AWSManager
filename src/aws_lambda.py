import boto3
import aws_session_handler
import json


# get all lambda functions of a region and return a list of functions
def get_lambda_functions(region):
    session = aws_session_handler.get_session()
    lambda_client = session.client('lambda', region_name=region)
    functions = lambda_client.list_functions()
    functions_list = []
    for lambdafunction in functions['Functions']:
        functions_list.append(lambdafunction)
    return functions_list


# get information about a lambda function
def get_lambda_function(region, function_name):
    session = aws_session_handler.get_session()
    lambda_client = session.client('lambda', region_name=region)
    lambdafunction = lambda_client.get_function(FunctionName=function_name)
    return lambdafunction


# invoke a lambda function
def invoke_lambda_function(region, function_name, payload):
    session = aws_session_handler.get_session()
    lambda_client = session.client('lambda', region_name=region)
    response = lambda_client.invoke(FunctionName=function_name, Payload=payload)
    return json.dumps(response, indent=2, default=str)
