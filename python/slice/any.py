class Hoge:
    def __getitem__(self, sl: slice):
        print(sl)


h = Hoge()
h["a":1.0:h]
# sliceオブジェクトには、何でも入れられる
