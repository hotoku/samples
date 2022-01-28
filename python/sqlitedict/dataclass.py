"""
dataclassは入らないぽい。
と思ったら、documentに、keyは、stringって書いてあった。
"""

from dataclasses import dataclass
from sqlitedict import SqliteDict


@dataclass
class Key:
    x: str
    y: int


@dataclass
class Value:
    a: str
    b: int
    c: float


with SqliteDict("db.sqlite") as dic:
    k = Key("a", 1)
    v = Value("a", 2, 3.0)
    dic[k] = v
