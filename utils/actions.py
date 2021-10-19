"""Utilities for GitHub Actions."""

import random

def random_weekly_cron_expr():
    return '{} {} {} {} {}'.format(
        random.randint(0, 59), # minute
        random.randint(0, 23), # hour
        '*',                   # day of month
        '*',                   # month
        random.randint(0, 6)   # day of week
    )
