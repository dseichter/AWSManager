import boto3
import aws_session_handler
import json


# get all cloudfront distributions and return a list of distributions
def get_cloudfront_distributions():
    session = aws_session_handler.get_session()
    cloudfront = session.client('cloudfront')
    distributions = cloudfront.list_distributions()
    distributions_list = []
    for distribution in distributions['DistributionList']['Items']:
        distributions_list.append(distribution)
    return distributions_list


# get information about a cloudfront distribution
def get_cloudfront_distribution(distribution_id):
    session = aws_session_handler.get_session()
    cloudfront = session.client('cloudfront')
    distribution = cloudfront.get_distribution(Id=distribution_id)
    return distribution


# invalidate a cloudfront distribution
def invalidate_cloudfront_distribution(distribution_id, paths):
    session = aws_session_handler.get_session()
    cloudfront = session.client('cloudfront')
    response = cloudfront.create_invalidation(DistributionId=distribution_id, InvalidationBatch={'Paths': {'Quantity': len(paths), 'Items': paths}, 'CallerReference': 'awsmanager'})
    return json.dumps(response, indent=2, default=str)


# load tags of a cloudfront distribution
def get_cloudfront_distribution_tags(distribution_id):
    session = aws_session_handler.get_session()
    cloudfront = session.client('cloudfront')
    tags = cloudfront.list_tags_for_resource(Resource=distribution_id)
    return tags
