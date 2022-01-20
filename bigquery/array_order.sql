WITH
  temp1 AS (
    SELECT
      ARRAY[1, 1, 1] AS xs,
      ARRAY[1, 2, 3] AS ys,
      ARRAY[30, 20, 10] AS zs
  ),
  temp2 AS (
    SELECT
      STRUCT(x, ys[OFFSET(off)] AS y, zs[OFFSET(off)] AS z) AS pairs
    FROM
      temp1,
      UNNEST(xs) AS x WITH OFFSET AS off
  ),
  temp3 AS (
    SELECT
      pairs.x AS x,
      pairs.y AS y,
      pairs.z AS z
    FROM
      temp2
  )
SELECT
  x,
  array_agg(y
    ORDER BY z) AS ys
FROM
  temp3
GROUP BY
  x;
