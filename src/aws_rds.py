import boto3
import aws_session_handler


# get all rds databases of a region and return a list of rds databases
def get_rds_databases(region):
    session = aws_session_handler.get_session()
    rds = session.client("rds", region_name=region)
    databases = rds.describe_db_instances()
    databases_list = []
    for database in databases["DBInstances"]:
        databases_list.append(database)
    return databases_list


def get_rds_database(region, db_instance_identifier):
    session = aws_session_handler.get_session()
    rds = session.client("rds", region_name=region)
    database = rds.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)
    return database["DBInstances"][0]


def start_rds_database(region, db_instance_identifier):
    session = aws_session_handler.get_session()
    rds = session.client("rds", region_name=region)
    response = rds.start_db_instance(DBInstanceIdentifier=db_instance_identifier)
    return response


def stop_rds_database(region, db_instance_identifier):
    session = aws_session_handler.get_session()
    rds = session.client("rds", region_name=region)
    response = rds.stop_db_instance(DBInstanceIdentifier=db_instance_identifier)
    return response


def reboot_rds_database(region, db_instance_identifier):
    session = aws_session_handler.get_session()
    rds = session.client("rds", region_name=region)
    response = rds.reboot_db_instance(DBInstanceIdentifier=db_instance_identifier)
    return response


def delete_rds_database(region, db_instance_identifier):
    session = aws_session_handler.get_session()
    rds = session.client("rds", region_name=region)
    response = rds.delete_db_instance(DBInstanceIdentifier=db_instance_identifier)
    return response
