#!/usr/bin/env python3

"""
Update the dates on the webpage.
"""

from datetime import date

import re


epoch = date(2025, 11, 15).toordinal()
offset = epoch % 14
today = date.today().toordinal()

dates = iter([
    str(date.fromordinal((((today - offset) // 14) + i) * 14 + offset))
    for i in range(0, 3)
])

DATE = r"[0-9]{4}-[0-9]{2}-[0-9]{2}"


with open("index.new.html", "w", encoding="utf-8") as fo:
    with open("index.html", "r", encoding="utf-8") as fi:
        for line in fi:
            fo.write(re.sub(DATE, lambda _match: next(dates), line))
