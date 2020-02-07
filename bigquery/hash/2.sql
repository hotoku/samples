#standardSQL


select
  mod(abs(farm_fingerprint(a)), 10)
from
  unnest([
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"10"
]) as a
  
