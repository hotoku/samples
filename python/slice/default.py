class Hoge:
    def __getitem__(self, sl: slice):
        print(sl)


h = Hoge()
h[:]
# => slice(None, None, None)
