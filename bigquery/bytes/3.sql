#standardSQL

select
  from_hex("01") > from_hex("00"),
  from_hex("01") > from_hex("0000"),
  from_hex("00") = from_hex("0000"),
  to_hex(b"1"),
  cast(to_hex(b"1") as int64)


-- +------+------+-------+-----+-----+
-- | f0_  | f1_  |  f2_  | f3_ | f4_ |
-- +------+------+-------+-----+-----+
-- | true | true | false | 31  |  31 |
-- +------+------+-------+-----+-----+

-- BYTES→INTの変換方法：to_hexでhexiadecimalにして、intにcast
-- hexadeximalで31をintに変換したら49になるのでは・・？？
