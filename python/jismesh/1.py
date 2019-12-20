import jismesh.utils as ju
import itertools as itt
import folium
import geojson as gj


# 緯度経度→メッシュコード
lat, lng = 35.658581, 139.745433
# 緯度経度→メッシュコード（レベルごと）
for i in range(6):
    code = ju.to_meshcode(lat, lng, i+1)
    print(f"{i+1}: {code}")


# メッシュコード→次数
print(f"resolution={ju.to_meshlevel(code)}")


# メッシュコード→緯度経度
# 南西を原点にして、緯度, 経度の方向に各単位だけずれた位置の緯度経度が返ってくる
# 
# to_meshcodeの第2, 3引数と、帰ってくるメッシュコードの位置関係
# (1, 0) -- (1, 1)
#  |            |
# (0, 0) -- (0, 1)
def to_lnglat_dict(code):
    sw = ju.to_meshpoint(code, 0, 0)
    se = ju.to_meshpoint(code, 0, 1)
    ne = ju.to_meshpoint(code, 1, 1)
    nw = ju.to_meshpoint(code, 1, 0)
    return dict(sw=sw, se=se,
                ne=ne, nw=nw)

def to_lnglat_list(code):
    sw = ju.to_meshpoint(code, 0, 0)
    se = ju.to_meshpoint(code, 0, 1)
    ne = ju.to_meshpoint(code, 1, 1)
    nw = ju.to_meshpoint(code, 1, 0)
    return [sw, se, ne, nw]


print(to_lnglat_dict(code))


def around(code, pos):
    """
    pos[0]: 緯度方向の移動単位
    pos[1]: 経度方向の移動単位
    """
    
    # (1,  -1)(1,  0)(1,  1)
    # (0,  -1)(0,  0)(0,  1)
    # (-1, -1)(-1, 0)(-1, 1)
    # に対して
    # (1.5,  -0.5)(1.5,  0.5)(1.5,  1.5)
    # (0.5,  -0.5)(0.5,  0.5)(0.5,  1.5)
    # (-0.5, -0.5)(-0.5, 0.5)(-0.5, 1.5)
    # を渡せば良い。つまり、それぞれの値に0.5を足して、to_meshpointに渡せば良さそう

    lnglat = ju.to_meshpoint(code, pos[0] + 0.5, pos[1] + 0.5)
    level = ju.to_meshlevel(code)
    return ju.to_meshcode(*lnglat, level)


for dx, dy in itt.product([-1, 0, 1], [-1, 0, 1]):
    print(to_lnglat_dict(around(code, (dx, dy))))



def swap_list(points):
    """
    (lat, lng)の配列を(lng, lat)の配列に変換する
    或いは
    (lng, lat)の配列を(lat, lng)の配列に変換する
    """
    return [(lng, lat) for (lat, lng) in points]

def make_polygon(latlng_list):
    print(f"make_polygon: {latlng_list}") 
    lnglat_list = swap_list(latlng_list)
    print(f"make_polygon-reversed: {lnglat_list}") 
    lnglat_ring = lnglat_list + [lnglat_list[0]]
    return gj.Polygon([lnglat_ring]) # 頂点の配列ではなく頂点の配列の配列を渡す

polygons = [
    make_polygon(to_lnglat_list(around(code, (dy, dx))))
    for (dy, dx)
    in itt.product([-1,0,1], [-1,0,1])
]
fcol = gj.FeatureCollection(
    features = [
        gj.Feature(geometry=poly, id=id)
        for (id, poly)
        in enumerate(polygons)
    ])
fmap = folium.Map((lat, lng), zoom_start=15, width=800, height=400)
folium.GeoJson(fcol, name="geojson").add_to(fmap)
fmap.save("1.html")    
