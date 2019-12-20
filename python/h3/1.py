from h3 import h3
import geojson as gj
import folium


lat, lng = 35.669469, 139.745842
res = 13


def swap_pair(pair):
    return pair[1], pair[0]


def loopify(pairs):
    return pairs + pairs[:1]


def polygon(lnglats):
    return gj.Polygon([lnglats])


def feature(i, polygon):
    return gj.Feature(
        geometry=polygon,
        id=i
    )


def save_map(fc):
    fmap = folium.Map((lat, lng), zoom_start=15, width=800, height=400)
    folium.GeoJson(fc, name="geojson").add_to(fmap)
    fmap.save("1.html")


def lmap(f, l):
    return list(map(f, l))


code = h3.geo_to_h3(lat, lng, res)  # str
code_set = h3.k_ring(code, 3)  # set(str)
verts_latlng = lmap(h3.h3_to_geo_boundary, code_set)  # [[pair]]
verts_lnglat = lmap(lambda x: lmap(swap_pair, x), verts_latlng)  # [[pair]]
rings = lmap(loopify, verts_lnglat)
polygons = lmap(polygon, rings)  # [polygon]
features = [feature(i, p) for i, p in enumerate(polygons)]
fc = gj.FeatureCollection(features)
save_map(fc)
