#standardSQL

create temp function func1(
  xs array<float64>
)
returns float64
language js as
"""
let ret = 0
for(i in xs){
  ret += xs[i]
}
return ret
""";

select func1([1,2,3.1])
