import urllib3
import json
import logging

VERSION = "v2024-06-09"
UPDATEURL = 'https://api.github.com/repos/dseichter/AWSManager/releases/latest'
RELEASES = 'https://github.com/dseichter/AWSManager/releases'
NAME = 'AWSManager'
LICENCE = 'GPL-3.0'


def check_for_new_release():
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', UPDATEURL)
        data = json.loads(r.data.decode('utf-8'))
        latest_version = data['tag_name']
        return latest_version != VERSION
    except Exception as e:
        logging.error(f"Error checking for new release: {e}")
        return False
