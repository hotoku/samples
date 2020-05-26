#standardSQL

select a.x, a.y from (
select struct(1 as x, 2 as y) as a
)
