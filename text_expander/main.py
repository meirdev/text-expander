from collections import deque
from typing import TypeAlias

from pynput import keyboard

from .matchs import MATCHES

Key: TypeAlias = keyboard.Key | keyboard.KeyCode
KeyHistory: TypeAlias = deque[Key]


def main() -> None:
    key_history: KeyHistory = deque(maxlen=200)

    controller = keyboard.Controller()

    with keyboard.Events() as events:
        for event in events:
            if isinstance(event, keyboard.Events.Press):
                if isinstance(event.key, keyboard.KeyCode):
                    key_history.append(event.key.char)
                else:
                    match event.key:
                        case keyboard.Key.backspace:
                            if len(key_history) > 0:
                                key_history.pop()
                        case keyboard.Key.space:
                            key_history.append(" ")
                        case keyboard.Key.enter:
                            key_history.append("\n")
                        case keyboard.Key.tab:
                            key_history.append("\t")
                        case _:
                            pass

            elif isinstance(event, keyboard.Events.Release):
                s = "".join(key_history)

                for match in MATCHES:
                    if result := match.check(s):
                        length, replace = result
                        for _ in range(length):
                            controller.tap(keyboard.Key.backspace)
                        controller.type(replace)
