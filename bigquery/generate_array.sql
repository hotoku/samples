SELECT
  xs
FROM
  UNNEST(generate_array(1, 10, 1)) AS xs;
-- => [1, 2, .., 10]

