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
import json

import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)


# get all cloudfront distributions and return a list of distributions
def get_cloudfront_distributions():
    logger.debug('START - get_cloudfront_distributions()')
    session = aws_session_handler.get_session()
    cloudfront = session.client('cloudfront')
    distributions = cloudfront.list_distributions()
    distributions_list = []
    for distribution in distributions['DistributionList']['Items']:
        distributions_list.append(distribution)
    return distributions_list


# get information about a cloudfront distribution
def get_cloudfront_distribution(distribution_id):
    logger.debug('START - get_cloudfront_distribution(distribution_id)')
    logger.debug('distribution_id: %s', distribution_id)
    session = aws_session_handler.get_session()
    cloudfront = session.client('cloudfront')
    distribution = cloudfront.get_distribution(Id=distribution_id)
    return distribution


# invalidate a cloudfront distribution
def invalidate_cloudfront_distribution(distribution_id, paths):
    logger.debug('START - invalidate_cloudfront_distribution(distribution_id, paths)')
    logger.debug('distribution_id: %s', distribution_id)
    logger.debug('paths: %s', paths)
    session = aws_session_handler.get_session()
    cloudfront = session.client('cloudfront')
    response = cloudfront.create_invalidation(DistributionId=distribution_id, InvalidationBatch={'Paths': {'Quantity': len(paths), 'Items': paths}, 'CallerReference': 'awsmanager'})
    return json.dumps(response, indent=2, default=str)


# load tags of a cloudfront distribution
def get_cloudfront_distribution_tags(distribution_id):
    logger.debug('START - get_cloudfront_distribution_tags(distribution_id)')
    logger.debug('distribution_id: %s', distribution_id)
    session = aws_session_handler.get_session()
    cloudfront = session.client('cloudfront')
    tags = cloudfront.list_tags_for_resource(Resource=distribution_id)
    return tags
