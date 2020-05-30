#standardSQL

create temp function func1(
  a struct<x int64, y int64>
)
returns int64
language js as
"""
return a.x + a.y // 文字列になってしまう
""";

select func1(struct(1 as x, 2 as y));
select func1(struct(1 as y, 2 as x)); -- 順番を変えても結果は変わらず。フィールドの名前ではなく位置が重要
-- select func1(struct(1 as x, 2 as y, 3 as z)); これはエラー
-- select func1(struct("1" as x, 2 as y)); これはエラー


-- https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions?hl=zh-tw
-- int64が入力としてサポートされてないぽい
