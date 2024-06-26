import boto3


# get all lambda functions of a region and return a list of functions
def get_lambda_functions(region):
    lambda_client = boto3.client('lambda', region_name=region)
    functions = lambda_client.list_functions()
    functions_list = []
    for function in functions['Functions']:
        functions_list.append(function)
    return functions_list
