#!/usr/bin/env python3

"""
Update the dates on the webpage.
"""

from datetime import date


epoch = date(2025, 11, 15).toordinal()
offset = epoch % 14
today = date.today().toordinal()

dates = [
    date.fromordinal((((today - offset) // 14) + i) * 14 + offset)
    for i in range(0, 3)
]

print(dates)
