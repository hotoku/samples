#!/usr/bin/env python

import base64


def main():
    with open("codama.png", "rb") as f:
        b1 = f.read()
    e1 = base64.b64encode(b1)
    print(e1)

    e2 = base64.b64encode(b1, altchars=b"-_")  # /+の代わりに-_を使う。ファイル名などにできる
    print(e2)


if __name__ == "__main__":
    main()
