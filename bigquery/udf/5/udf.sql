#standardSQL



create temp function func1(
  x float64
)
returns float64
language js as
"""
  return foo(x)
"""
options  (
  library="gs://us-central1-dev-004-5acd9ac2-bucket/f.js"
)
;

select func1(1), func1(2)
