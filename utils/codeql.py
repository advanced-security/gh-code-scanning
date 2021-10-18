"""Utilities for CodeQL."""

import json
import subprocess

def get_codeql_langs(gh, nwo):
    """
    Obtain the programming languages that GitHub detected in the repo nwo.
    Then, filter the languages down to the CodeQL supported languages, and
    transform them to the CodeQL language identifiers.
    """
    cmd = subprocess.run([gh, 'api', f'repos/{nwo}/languages'], capture_output=True)
    for lang in json.loads(cmd.stdout):
        if lang in ['C', 'C++']:
            yield 'cpp'
        elif lang == 'Java':
            yield 'java'
        elif lang == 'C#':
            yield 'csharp'
        elif lang == 'Go':
            yield 'go'
        elif lang == 'Python':
            yield 'python'
        elif lang in ['JavaScript', 'TypeScript']:
            yield 'javascript'
