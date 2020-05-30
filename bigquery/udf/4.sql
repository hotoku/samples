#standardSQL

create temp function func1(
  a struct<x float64, y float64>
)
returns float64
language js as
"""
return 10 * a.x + a.y
""";

select func1(struct(1 as x, 2 as y));
select func1(struct(1 as y, 2 as x)); -- やはり位置が重要
