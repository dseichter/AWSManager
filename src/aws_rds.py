import boto3
import aws_session_handler


# get all rds databases of a region and return a list of rds databases
def get_rds_databases(region):
    session = aws_session_handler.get_session()
    rds = session.client('rds', region_name=region)
    databases = rds.describe_db_instances()
    databases_list = []
    for database in databases['DBInstances']:
        databases_list.append(database)
    return databases_list
