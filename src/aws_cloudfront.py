import boto3


# get all cloudfront distributions and return a list of distributions
def get_cloudfront_distributions():
    cloudfront = boto3.client('cloudfront')
    distributions = cloudfront.list_distributions()
    distributions_list = []
    for distribution in distributions['DistributionList']['Items']:
        distributions_list.append(distribution)
    return distributions_list
