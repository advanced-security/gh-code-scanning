"""Miscellaneous utilities"""

import os
import subprocess

def get_parent_exe():
    try:
        ps = subprocess.run(['ps', '-oargs=', '-p', str(os.getppid())], capture_output=True, check=True)
        return ps.stdout.decode('UTF-8').split()[0]
    except subprocess.CalledProcessError:
        return None
