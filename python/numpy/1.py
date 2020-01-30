import numpy as np
import h3.h3 as h3

"""
普通の関数をユニバーサル関数に変換する
"""


lat = np.array([35, 35])
lng = np.array([139, 139])

# print(h3.geo_to_h3(lat, lng, 13))  # これだとエラー

g2h3 = np.frompyfunc(h3.geo_to_h3, 3, 1)
print(g2h3(lat, lng, 13))
