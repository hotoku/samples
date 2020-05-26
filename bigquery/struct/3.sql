#standardSQL


select a.x + a.y from (
select struct(x as x, y as y) as a from unnest([1,2,3]) as x, unnest([4,5,6]) as y
)
