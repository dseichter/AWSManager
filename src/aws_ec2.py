import boto3


# get information about an ec2 instance
def get_ec2_instance(region, instance_id):
    ec2 = boto3.client('ec2', region_name=region)
    instance = ec2.describe_instances(InstanceIds=[instance_id])
    return instance['Reservations'][0]['Instances'][0]


# get all information about a volumeid
def get_ec2_volume(region, volume_id):
    ec2 = boto3.client('ec2', region_name=region)
    volume = ec2.describe_volumes(VolumeIds=[volume_id])
    return volume['Volumes'][0]


# get all ec2 instances of a region and return a list of instances
def get_ec2_instances(region):
    ec2 = boto3.client('ec2', region_name=region)
    instances = ec2.describe_instances()
    instances_list = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instances_list.append(instance)
    return instances_list
