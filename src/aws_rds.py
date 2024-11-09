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

import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)


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
