"""Utilitarian functions for the use of the GitHub API."""

import json
import subprocess

def get_repo_default_branch(gh, nwo):
    cmd = subprocess.run([gh, 'api', f'repos/{nwo}'], capture_output=True)
    return json.loads(cmd.stdout)['default_branch']

def get_repo_cs_alerts(gh, nwo):
    # json_multiloads decodes multiple JSON documents that have
    # been concatenated together, as `gh api --paginate` does.
    # See: https://github.com/cli/cli/issues/1268.
    def json_multiloads(json_string, spool=[]):
        try:
            spool += json.loads(json_string)
        except json.decoder.JSONDecodeError as e:
            spool += json.loads(json_string[:e.pos])
            json_multiloads(json_string[e.pos:], spool)
        return spool

    cmd = subprocess.run([gh, 'api', '--paginate', f'repos/{nwo}/code-scanning/alerts'], capture_output=True, check=True)
    return json_multiloads(cmd.stdout)

def get_repo_langs(gh, nwo):
    cmd = subprocess.run([gh, 'api', f'repos/{nwo}/languages'], capture_output=True)
    return json.loads(cmd.stdout)
