#!/usr/bin/env python

import sys
from collections import deque


class Buffer:
    size = 2

    def __init__(self) -> None:
        self.q: deque[str] = deque()

    def append(self, l: str):
        if len(self.q) == self.size:
            self.q.popleft()
        self.q.append(l)

    def __getitem__(self, n) -> str:
        ret = self.q[n]
        return ret

    def __len__(self) -> int:
        return len(self.q)


def main():
    buf = Buffer()
    for l in sys.stdin.readlines():
        buf.append(l)
        print(l, end="")
        if len(buf) < 2:
            continue
        if buf[1].strip() == '<script src="https://unpkg.com/reveal.js@^4//plugin/math/math.js"></script>':
            print('<script src="plugin/menu/menu.js"></script>')
        if buf[0].strip() == '// reveal.js plugins' and \
           buf[1].strip() == 'plugins: [':
            print("RevealMenu,")


if __name__ == "__main__":
    main()
