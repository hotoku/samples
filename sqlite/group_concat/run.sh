#!/bin/bash


rm -f db.sqlite


cat <<EOF | sqlite3
create table sample (
  x integer,
  y text,
  z integer
);


insert into sample (x, y, z)
values
  (1, "a", 1),
  (1, "b", 2),
  (2, "c", 2),
  (2, "d", 1);


select distinct
  x,
  group_concat(y, "-")
    over (
      partition by x
      order by z
      rows between unbounded preceding and unbounded following
    ) as y
from
  sample;
EOF
