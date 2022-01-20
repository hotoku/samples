WITH
  temp1 AS (
    SELECT
      x,
      y
    FROM
      UNNEST(ARRAY[1, 2, 3]) AS x,
      UNNEST(ARRAY[11, 12, 13]) AS y
  )
SELECT
  x,
  count(1) AS cnt,
  countif(y <= 12) AS cntif,
  countif(y <= 12) / count(1) AS ratio
FROM
  temp1
GROUP BY
  x;
