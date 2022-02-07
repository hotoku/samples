---
title: sample slide
author: 堀越 保徳
date: 2022-02-07
---

# サマリ

## 箇条書き

- ろーれむ・いぷさむ
- 銀河鉄道の夜
- 吾輩は猫である

## 数字付きリスト

1. あれ
2. これ
3. それ・・など

# 数式を書いてみる

確率変数 \\(X\\) が正規分布に従うとき、確率密度関数 \\(f(x) \\)は、

\\[ f(x) = \\frac {1} {\\sqrt{2\\pi\\sigma^2}} \\exp\\left( -\\frac{ (x-\\mu)^2 }{2\\sigma^2 } \\right)  \\]

# コードを書いてみる

```python
import click

@click.command()
def main():
    print("Hello World !")

if __name__ == "__file__":
    main()
```

# 絵を入れてみる

![横浜の写真](resource/yokohama.jpg){ width=250px }

# リンクを入れてみる

- [stack overflow](https://stackoverflow.com/)
- [Google](https://www.google.com/)
