import json
import boto3
import os

CONFIGFILE = "config.json"


def create_config():
    # create the config file if it does not exist
    try:
        with open(CONFIGFILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        with open(CONFIGFILE, "w") as f:
            f.write("{}")

    with open(CONFIGFILE, "r") as f:
        data = json.load(f)

    if "aws_access_key_id" not in data:
        data["aws_access_key_id"] = ""
    if "aws_secret_access_key" not in data:
        data["aws_secret_access_key"] = ""
    if "aws_session_token" not in data:
        data["aws_session_token"] = ""
    if "aws_profile" not in data:
        data["aws_profile"] = ""
    if "region" not in data:
        data["region"] = "eu-central-1"

    with open(CONFIGFILE, "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)


def read_config():
    with open(CONFIGFILE, "r") as f:
        return json.load(f)


def save_config(key, value):
    with open(CONFIGFILE, "r") as f:
        data = json.load(f)
        data[key] = value
    with open(CONFIGFILE, "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)


# get a list of all AWS profiles of the credentials file
def get_profiles():
    profiles = []
    if os.name == "posix":  # Linux or macOS
        credentials_file = os.path.expanduser("~/.aws/credentials")
    elif os.name == "nt":  # Windows
        credentials_file = os.path.expanduser(
            os.path.join(os.environ["USERPROFILE"], ".aws", "credentials")
        )
    else:
        raise OSError("Unsupported operating system")

    with open(credentials_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("["):
                profile = line.strip().strip("[]")
                profiles.append(profile)
    return profiles


# get a list of all AWS regions using the boto3 library
def get_regions():
    ec2 = boto3.client("ec2")
    regions = ec2.describe_regions()
    region_list = []
    for region in regions["Regions"]:
        region_list.append(region["RegionName"])
    return region_list
