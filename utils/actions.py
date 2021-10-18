"""Utilities for GitHub Actions."""

import random

def random_weekly_cron_expr():
    return '{} {} * {} {}'.format(
        random.randint(0, 59), # minute
        random.randint(0, 23), # hour
        random.randint(1, 12), # month
        random.randint(0, 6)   # day of week
    )
