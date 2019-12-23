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

fmap = folium.Map((lat, lng), zoom_start=20)
folium.GeoJson(
    polygon(center),
    name="poly").add_to(fmap)
fmap.save("1.html")
