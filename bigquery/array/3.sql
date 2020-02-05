#standardSQL

-- 1.sqlのレコード数をカウントしてみる

with t as (
  select 1 as a, [1,2,3] as b
)
select
  count(1)
from
  t, unnest(b)


-- +-----+
-- | f0_ |
-- +-----+
-- |   3 |
-- +-----+
