from abc import ABC, abstractmethod


class Singer(ABC):
    @abstractmethod
    def sing(self):
        return NotImplemented


class Dancer(ABC):
    @abstractmethod
    def dance(self):
        return NotImplemented


class DanceUnit(Singer, Dancer):
    def play(self):
        self.sing()
        self.dance()


class BadSinger(Singer):
    pass


class GoodSinger(Singer):
    def sing(self):
        print("I can sing", end=" ")


class JazzDancer(Dancer):
    def dance(self):
        print("jazz jazz")


class BadUnit(DanceUnit, BadSinger, JazzDancer):
    pass


class GoodUnit(DanceUnit, GoodSinger, JazzDancer):
    pass


# bunit = BadUnit()
# > Traceback (most recent call last):
# > File "abc_dance_unit.py", line 44, in <module>
# >     bunit = BadUnit()
# >     TypeError: Can't instantiate abstract class BadUnit with abstract methods sing
gunit = GoodUnit()
gunit.play()
