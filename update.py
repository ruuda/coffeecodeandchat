#!/usr/bin/env python3

"""
Update the dates on the webpage.
"""

from datetime import date

import os
import re


epoch = date(2025, 11, 15).toordinal()
offset = epoch % 14
today = date.today().toordinal()

dates = iter([
    str(date.fromordinal((((today - offset) // 14) + i) * 14 + offset))
    for i in range(1, 4)
])

DATE = r"[0-9]{4}-[0-9]{2}-[0-9]{2}"


with open("index.html", "r", encoding="utf-8") as fi:
    with open("index.new.html", "w", encoding="utf-8") as fo:
        for line in fi:
            fo.write(re.sub(DATE, lambda _match: next(dates), line))

os.rename("index.new.html", "index.html")
