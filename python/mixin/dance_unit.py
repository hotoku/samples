class JapaneseSinger:
    def sing(self):
        print("私は歌う", end=" ")


class EnglishSinger:
    def sing(self):
        print("I sing", end=" ")


class JazzDancer:
    def dance(self):
        print("jazz jazz")


class LockDancer:
    def dance(self):
        print("lock lock")


class DanceUnit:
    def play(self):
        self.sing()
        self.dance()


class JpJazzUnit(DanceUnit, JapaneseSinger, JazzDancer):
    pass


class JpLocUnit(DanceUnit, JapaneseSinger, LockDancer):
    pass


class EnJazzUnit(DanceUnit, EnglishSinger, JazzDancer):
    pass


class EnLocUnit(DanceUnit, EnglishSinger, LockDancer):
    pass


jj = JpJazzUnit()
jl = JpLocUnit()
ej = EnJazzUnit()
el = EnLocUnit()

jj.play()
jl.play()
ej.play()
el.play()
