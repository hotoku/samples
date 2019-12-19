import sqlite3


con = sqlite3.connect(":memory:")

cur = con.cursor()
cur.executescript("""
create table x (
  id integer primary key autoincrement,
  val integer,
  key text
);
""")
con.commit()

cur.executemany("""
insert into x(val, key) values(?, ?);
""", [(1, "a"),
      (2, "b")])
con.commit()


ret = cur.execute("""
select * from x;
""")


for c in ret:
    print(c)

# 素でやるとタプルで返ってくる
# row_factoryを指定すると辞書型になる

con.row_factory = sqlite3.Row
cur = con.cursor()

ret = cur.execute("""
select * from x;
""")


for c in ret:
    print(f"{c['id']}, {c['val']}, {c['key']}")


# 0行の場合には何が返ってくるのか
ret = cur.execute("""
select * from x where id = 1000;
""")

print(ret)

# 答え：Cursorオブジェクト
for r in ret:
    print(r)
