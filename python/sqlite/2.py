import sqlite3

"""
sqliteのTrueとFalseが何で返ってくるか
答え：TRUE=1, FALSE=0
"""


con = sqlite3.connect(":memory:")
con.row_factory = sqlite3.Row
cur = con.cursor()
ret = cur.execute("""
select null is null as t, null is not null as f;
""")

for c in ret:
    print(f"TRUE={c['t']}, FALSE={c['f']}")
