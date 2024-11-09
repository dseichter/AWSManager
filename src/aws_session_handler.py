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
import settings

import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)


# use the selected profile, if no profile is given, use the default profile or the provided credentials
def get_session():
    awslogin = settings.read_config()
    aws_access_key_id = awslogin.get("aws_access_key_id", None)
    aws_secret_access_key = awslogin.get("aws_secret_access_key", None)
    aws_session_token = awslogin.get("aws_session_token", None)
    aws_profile = awslogin.get("aws_profile", None)
    if aws_access_key_id and aws_secret_access_key:
        session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
        )
    elif aws_profile:
        session = boto3.Session(profile_name=aws_profile)
    return session
