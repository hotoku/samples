---
title:
- sample slide
author:
- 堀越 保徳
date:
- 2022-02-07

---

# サマリ

- ろーれむ・いぷさむ
- 銀河鉄道の夜
- 吾輩は猫である

# 数式を書いてみる

確率変数$X$が正規分布に従うとき、$X$の確率密度関数は・・
$$
\mathrm{Pr}(x \le X < x + \mathrm{d}x)
$$

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

横浜の写真

![横浜](resource/yokohama.jpg){ width=250px }
