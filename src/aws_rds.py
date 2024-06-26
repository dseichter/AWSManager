import boto3


# get all rds databases of a region and return a list of rds databases
def get_rds_databases(region):
    rds = boto3.client('rds', region_name=region)
    databases = rds.describe_db_instances()
    databases_list = []
    for database in databases['DBInstances']:
        databases_list.append(database)
    return databases_list
