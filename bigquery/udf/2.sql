#standardSQL

create temp function func1(
)
returns float64
language js as
"""
return Math.PI
""";

select func1()
