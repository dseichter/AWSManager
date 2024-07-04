import boto3


# get all s3 buckets of a region and return a list of buckets
def get_s3_buckets(region):
    s3 = boto3.client('s3', region_name=region)
    buckets = s3.list_buckets()
    buckets_list = []
    for bucket in buckets['Buckets']:
        buckets_list.append(bucket)
    return buckets_list


# get all objects of a bucket
def get_s3_bucket_objects(region, bucket_name):
    s3 = boto3.client('s3', region_name=region)
    objects = s3.list_objects_v2(Bucket=bucket_name)
    objects_list = []
    for obj in objects['Contents']:
        objects_list.append(obj)
    return objects_list


# download an object from a bucket into given file
def download_object(region, bucket_name, object_name, file_name):
    s3 = boto3.client('s3', region_name=region)
    s3.download_file(bucket_name, object_name, file_name)


# upload a file to a bucket
def upload_file(region, bucket_name, file_name, object_name):
    s3 = boto3.client('s3', region_name=region)
    s3.upload_file(file_name, bucket_name, object_name)


# delete an object from a bucket
def delete_object(region, bucket_name, object_name):
    s3 = boto3.client('s3', region_name=region)
    s3.delete_object(Bucket=bucket_name, Key=object_name)
