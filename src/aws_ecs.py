import boto3
import aws_session_handler


# get all ECS clusters of a region and return a list of ECS clusters
def get_ecs_clusters(region):
    session = aws_session_handler.get_session()
    ecs = session.client("ecs", region_name=region)
    clusters = ecs.list_clusters()
    clusters_list = []
    for cluster in clusters["clusterArns"]:
        clusters_list.append(cluster)
    return clusters_list


# get all ECS services of a cluster and return a list of ECS services
def get_ecs_services(region, cluster):
    session = aws_session_handler.get_session()
    ecs = session.client("ecs", region_name=region)
    services = ecs.list_services(cluster=cluster)
    services_list = []
    for service in services["serviceArns"]:
        services_list.append(service)
    return services_list


# get all ECS tasks of a service and return a list of ECS tasks
def get_ecs_tasks(region, cluster, service):
    session = aws_session_handler.get_session()
    ecs = session.client("ecs", region_name=region)
    tasks = ecs.list_tasks(cluster=cluster, serviceName=service)
    tasks_list = []
    for task in tasks["taskArns"]:
        tasks_list.append(task)
    return tasks_list


# load the details of the service
def get_ecs_service_details(region, cluster, service):
    session = aws_session_handler.get_session()
    ecs = session.client("ecs", region_name=region)
    service_details = ecs.describe_services(cluster=cluster, services=[service])
    return service_details


# set the desired count of a service
def set_ecs_desired_count(region, cluster, service, count):
    session = aws_session_handler.get_session()
    ecs = session.client("ecs", region_name=region)
    response = ecs.update_service(cluster=cluster, service=service, desiredCount=count)
    return response
