
```
* 817d784 Revert "3" (Yasunori Horikoshi: 2022/02/04 16:51:07)  (HEAD -> main)
* bee294a Revert "4" (Yasunori Horikoshi: 2022/02/04 16:50:53)
* bd3e644 4 (Yasunori Horikoshi: 2022/02/04 16:50:23)
* 894689c 3 (Yasunori Horikoshi: 2022/02/04 16:50:15)
* 61d01a5 2 (Yasunori Horikoshi: 2022/02/04 16:50:08)
* 3c7296f 1 (Yasunori Horikoshi: 2022/02/04 16:49:58)
```

`HEAD=bd3e644`の状態で、

```shell
git revert HEAD~2..HEAD
```

↑を実行すると、4,3を打ち消すrevertが発行された
