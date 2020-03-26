#!/usr/bin/env python

import base64


def main():
    s1 = b"abcdefghijklmnopqrstuvwxyz+*}{`!  # $%&'()=~|^\""
    e1 = base64.b64encode(s1)
    print(e1)

    s2 = "あいうえお".encode("utf-8")
    e2 = base64.b64encode(s2)
    print(e2)


if __name__ == "__main__":
    main()
