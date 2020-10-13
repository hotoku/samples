## クローリング

```
$ cd jalan
$ mkdir data
$ scrapy crawl PoiCollector
```

jalan/dataの下に、poiの情報が集まる。

## Geocoding

上のクローリングを行ったあとに以下を叩く。

```
$ ./geocoding2.py
```

list.csvができる。

## Geocoding（非同期版）

```
$ ./geocoding.py
```

こちらのスクリプトでは、非同期にAPIを叩く。geocoding2より10倍くらい早い（はず）。
