import folium
from h3 import h3
import geojson as gj


def loop(ls):
    return ls + ls[:1]


def swap(p):
    return p[1], p[0]


def polygon(h3id):
    latlngs = h3.h3_to_geo_boundary(h3id)
    looped = loop(latlngs)
    lnglats = [swap(i) for i in looped]
    return gj.Polygon([lnglats])


def feature_collection(polys):
    features = [
        gj.Feature(geometry=p, id=i)
        for i, p in enumerate(polys)
    ]
    return gj.FeatureCollection(features)


lat, lng = 35, 139
res = 10
center = h3.geo_to_h3(lat, lng, 10)
around = h3.k_ring(center, 10)
polys = [polygon(i) for i in around]
fc_list = [feature_collection([i]) for i in polys]


fmap = folium.Map((lat, lng), zoom_start=20)
for fc, code in zip(fc_list, around):
    temp = folium.GeoJson(fc)
    folium.Popup(code).add_to(temp)
    temp.add_to(fmap)

fmap.save("3.html")
