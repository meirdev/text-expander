import re
from dataclasses import dataclass
from typing import Callable


@dataclass
class Match:
    trigger: str | re.Pattern
    replace: str | Callable[[str], str]

    def value(self, s: str | tuple[str, ...]) -> str:
        if isinstance(self.replace, str):
            return self.replace
        else:
            return self.replace(s)

    def check(self, s: str) -> tuple[int, str] | None:
        if isinstance(self.trigger, str):
            if s.endswith(self.trigger):
                return len(self.trigger), self.value(self.trigger)
        else:
            match = self.trigger.search(s)
            if match:
                return match.end() - match.start(), self.value(match.groups())
