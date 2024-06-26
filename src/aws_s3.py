import boto3


# get all s3 buckets of a region and return a list of buckets
def get_s3_buckets(region):
    s3 = boto3.client('s3', region_name=region)
    buckets = s3.list_buckets()
    buckets_list = []
    for bucket in buckets['Buckets']:
        buckets_list.append(bucket)
    return buckets_list
