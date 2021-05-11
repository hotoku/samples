#standardSQL

with temp1 as (
    select x, y from unnest([1,2,3]) x, unnest(["a", "b", "c"]) y
)
select * from temp1 pivot(SUM(x) for y in ("a", "b", "c"))


-- +---+---+---+
-- | a | b | c |
-- +---+---+---+
-- | 6 | 6 | 6 |
-- +---+---+---+

