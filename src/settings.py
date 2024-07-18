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
    if "load_on_startup" not in data:
        data["load_on_startup"] = False
    if "check_for_updates" not in data:
        data["check_for_updates"] = True

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
