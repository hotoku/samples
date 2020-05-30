#standardSQL

create temp function func(
  a float64
)
returns float64
language js as
"""
{% include "sample-var.js" %}
return sample.b(a)
""";

select func(1)

