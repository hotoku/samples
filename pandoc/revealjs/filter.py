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
        if len(buf) < 2:
            print(l, end="")
            continue
        elif buf[1].strip() == '<script src="https://unpkg.com/reveal.js@^4//plugin/math/math.js"></script>':
            print(l, end="")
            print('<script src="plugin/menu/menu.js"></script>')
        elif buf[0].strip() == '// reveal.js plugins' and \
                buf[1].strip() == 'plugins: [':
            print(l, end="")
            print("RevealMenu,")
        elif buf[1].strip() == '<link rel="stylesheet" href="https://unpkg.com/reveal.js@^4//dist/theme/black.css" id="theme">':
            print("""
<link rel="stylesheet" href="https://unpkg.com/reveal.js@^4//dist/theme/white.css" id="theme">
<style>
  ul li {
      padding-bottom:0.4em;
  }
  ol li {
      padding-bottom:0.4em;
  }
  :root {
      --r-heading1-size: 1.2em;
      --r-heading-text-transform: none;
      --r-main-font-size: 34px;
  }
</style>
""")
        else:
            print(l, end="")


if __name__ == "__main__":
    main()
