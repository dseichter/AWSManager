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


# get all ECS clusters of a region and return a list of ECS clusters
def get_ecs_clusters(region):
    logger.debug('START - get_ecs_clusters(region)')
    logger.debug('region: %s', region)
    session = aws_session_handler.get_session()
    ecs = session.client("ecs", region_name=region)
    clusters = ecs.list_clusters()
    clusters_list = []
    for cluster in clusters["clusterArns"]:
        clusters_list.append(cluster)
    return clusters_list


# get all ECS services of a cluster and return a list of ECS services
def get_ecs_services(region, cluster):
    logger.debug('START - get_ecs_services(region, cluster)')
    logger.debug('region: %s', region)
    logger.debug('cluster: %s', cluster)
    session = aws_session_handler.get_session()
    ecs = session.client("ecs", region_name=region)
    services = ecs.list_services(cluster=cluster)
    services_list = []
    for service in services["serviceArns"]:
        services_list.append(service)
    return services_list


# get all ECS tasks of a service and return a list of ECS tasks
def get_ecs_tasks(region, cluster, service):
    logger.debug('START - get_ecs_tasks(region, cluster, service)')
    logger.debug('region: %s', region)
    logger.debug('cluster: %s', cluster)
    logger.debug('service: %s', service)
    session = aws_session_handler.get_session()
    ecs = session.client("ecs", region_name=region)
    tasks = ecs.list_tasks(cluster=cluster, serviceName=service)
    tasks_list = []
    for task in tasks["taskArns"]:
        tasks_list.append(task)
    return tasks_list


# load the details of the service
def get_ecs_service_details(region, cluster, service):
    logger.debug('START - get_ecs_service_details(region, cluster, service)')
    logger.debug('region: %s', region)
    logger.debug('cluster: %s', cluster)
    logger.debug('service: %s', service)
    session = aws_session_handler.get_session()
    ecs = session.client("ecs", region_name=region)
    service_details = ecs.describe_services(cluster=cluster, services=[service])
    return service_details


# set the desired count of a service
def set_ecs_desired_count(region, cluster, service, count):
    logger.debug('START - set_ecs_desired_count(region, cluster, service, count)')
    logger.debug('region: %s', region)
    logger.debug('cluster: %s', cluster)
    logger.debug('service: %s', service)
    logger.debug('count: %s', count)
    session = aws_session_handler.get_session()
    ecs = session.client("ecs", region_name=region)
    response = ecs.update_service(cluster=cluster, service=service, desiredCount=count)
    return response
