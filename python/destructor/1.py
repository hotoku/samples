class Hoge:
    def __del__(self):
        print("deleting Hoge")


h = Hoge()
raise Exception()
