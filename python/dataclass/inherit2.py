from typing import Dict, Any
from dataclasses import dataclass


class Parameter:
    def to_dict(self) -> Dict[str, Any]:
        keys = [
            key for key in dir(self)
            if (not key[:2] == "__") and (not key == "to_dict")
        ]
        return {
            k: getattr(self, k)
            for k in keys
        }


@dataclass
class Param1(Parameter):
    x: int
    y: str


p1 = Param1(1, "a")
print(p1.to_dict())
