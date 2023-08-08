import re
from datetime import datetime

from .match import Match


MATCHES = [
    Match(":today", lambda _: datetime.today().strftime("%Y-%m-%d")),
    Match(re.compile(r"(\d+)\s*\+\s*(\d+)\s*="), lambda m: str(int(m[0]) + int(m[1]))),
]
