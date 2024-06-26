import boto3


# get all ec2 instances of a region and return a list of instances
def get_ec2_instances(region):
    ec2 = boto3.client('ec2', region_name=region)
    instances = ec2.describe_instances()
    instances_list = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instances_list.append(instance)
    return instances_list
