"""Utilities for CodeQL."""

import json
import subprocess

languages = {'C', 'C++', 'Java', 'C#', 'Go', 'Python', 'Javascript', 'TypeScript'}

def normalize_lang(lang):
    """
    CodeQL uses certain keywords to identify a language. These keywords are typically
    not the language name itself. So, this function maps the programming-language
    name to the CodeQL language keyword.
    """
    if lang in {'C', 'C++'}:
        return 'cpp'
    elif lang == 'Java':
        return 'java'
    elif lang == 'C#':
        return 'csharp'
    elif lang == 'Go':
        return 'go'
    elif lang == 'Python':
        return 'python'
    elif lang in {'JavaScript', 'TypeScript'}:
        return 'javascript'
