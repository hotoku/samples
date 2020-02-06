#standardSQL

-- 点が多角形に含まれているかどうか？

select *, st_contains(poly, p) as flag from (
select ST_GeogFromGeoJSON('{"coordinates": [[ [1,1], [1,2], [2,2], [2,1], [1,1] ]],  "type": "Polygon"}') as poly
) l , unnest([
   st_geogpoint(1.5, 1.5),
   st_geogpoint(3, 3)
]) as p
