import boto3
import settings


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
