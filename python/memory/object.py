from dataclasses import dataclass
import sys

import numpy as np


@dataclass
class Week:
    year: int
    week: int


w1 = Week(2020, 1)
print(sys.getsizeof(w1))  # => 48

a1 = np.arange(10)
print(sys.getsizeof(a1))  # => 184

a2 = np.arange(20)
print(sys.getsizeof(a2))  # => 264

a3 = np.arange(30)
print(sys.getsizeof(a3))  # => 344

aw1 = np.array([Week(2020, i) for i in range(10)])
print(sys.getsizeof(aw1))  # => 184

aw2 = np.array([Week(2020, i) for i in range(20)])
print(sys.getsizeof(aw2))  # => 264

# np.arrayもポインタ持っているだけなので、実際のサイズが分からんな


@dataclass
class Int3:
    i1: int
    i2: int
    i3: int


i31 = Int3(300, 300, 300)
print(sys.getsizeof(i31))  # => 48

# ということは、Weekが実際に、どれだけメモリ使ってるのかも分からんな・・

# Local Variables:
# lsp-pyright-venv-path: "/Users/hotoku/.pyenv/versions/3.9.5/envs/global"
# End:
