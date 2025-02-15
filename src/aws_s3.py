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


# get all s3 buckets of a region and return a list of buckets
def get_s3_buckets(region):
    logger.debug('START - get_s3_buckets(region)')
    logger.debug('region: %s', region)
    session = aws_session_handler.get_session()
    s3 = session.client('s3', region_name=region)
    buckets = s3.list_buckets()
    buckets_list = []
    for bucket in buckets['Buckets']:
        buckets_list.append(bucket)
    return buckets_list


# get all objects of a bucket
def get_s3_bucket_objects(region, bucket_name):
    logger.debug('START - get_s3_bucket_objects(region, bucket_name)')
    logger.debug('region: %s', region)
    logger.debug('bucket_name: %s', bucket_name)
    s3 = boto3.client('s3', region_name=region)
    objects = s3.list_objects_v2(Bucket=bucket_name)
    objects_list = []
    for obj in objects['Contents']:
        objects_list.append(obj)
    return objects_list


# download an object from a bucket into given file
def download_object(region, bucket_name, object_name, file_name):
    logger.debug('START - download_object(region, bucket_name, object_name, file_name)')
    logger.debug('region: %s', region)
    logger.debug('bucket_name: %s', bucket_name)
    logger.debug('object_name: %s', object_name)
    logger.debug('file_name: %s', file_name)
    session = aws_session_handler.get_session()
    s3 = session.client('s3', region_name=region)
    s3.download_file(bucket_name, object_name, file_name)


# upload a file to a bucket
def upload_file(region, bucket_name, file_name, object_name):
    logger.debug('START - upload_file(region, bucket_name, file_name, object_name)')
    logger.debug('region: %s', region)
    logger.debug('bucket_name: %s', bucket_name)
    logger.debug('file_name: %s', file_name)
    logger.debug('object_name: %s', object_name)
    session = aws_session_handler.get_session()
    s3 = session.client('s3', region_name=region)
    s3.upload_file(file_name, bucket_name, object_name)


# delete an object from a bucket
def delete_object(region, bucket_name, object_name):
    logger.debug('START - delete_object(region, bucket_name, object_name)')
    logger.debug('region: %s', region)
    logger.debug('bucket_name: %s', bucket_name)
    logger.debug('object_name: %s', object_name)
    session = aws_session_handler.get_session()
    s3 = session.client('s3', region_name=region)
    s3.delete_object(Bucket=bucket_name, Key=object_name)
