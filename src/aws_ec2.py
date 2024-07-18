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


# get information about an ec2 instance
def get_ec2_instance(region, instance_id):
    session = aws_session_handler.get_session()
    ec2 = session.client('ec2', region_name=region)
    instance = ec2.describe_instances(InstanceIds=[instance_id])
    return instance['Reservations'][0]['Instances'][0]


# get all information about a volumeid
def get_ec2_volume(region, volume_id):
    session = aws_session_handler.get_session()
    ec2 = session.client('ec2', region_name=region)
    volume = ec2.describe_volumes(VolumeIds=[volume_id])
    return volume['Volumes'][0]


# get all ec2 instances of a region and return a list of instances
def get_ec2_instances(region):
    session = aws_session_handler.get_session()
    ec2 = session.client('ec2', region_name=region)
    instances = ec2.describe_instances()
    instances_list = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instances_list.append(instance)
    return instances_list


# start a given instance
def start_ec2_instance(region, instance_id):
    session = aws_session_handler.get_session()
    ec2 = session.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=[instance_id])


# stop a given instance
def stop_ec2_instance(region, instance_id):
    session = aws_session_handler.get_session()
    ec2 = session.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=[instance_id])


# reboot a given instance
def reboot_ec2_instance(region, instance_id):
    session = aws_session_handler.get_session()
    ec2 = session.client('ec2', region_name=region)
    ec2.reboot_instances(InstanceIds=[instance_id])


# terminate a given instance
def terminate_ec2_instance(region, instance_id):
    session = aws_session_handler.get_session()
    ec2 = session.client('ec2', region_name=region)
    ec2.terminate_instances(InstanceIds=[instance_id])
