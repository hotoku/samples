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


good_unit = GoodUnit()
good_unit.play()

bad_unit = BadUnit()
# > Traceback (most recent call last):
# >   File "abc_dance_unit.py", line 47, in <module>
# >       bad_unit = BadUnit()
# >       TypeError: Can't instantiate abstract class BadUnit with abstract methods sing
