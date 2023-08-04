import sqlite3


with sqlite3.connect(":memory:") as con:
    con.executescript("""
    create table x (
      id integer primary key,
      x text not null
    );
    insert into x (x) values ("x");
    insert into x (x) values ("y");
    insert into x (x) values ("z");
    """)
    con.commit()

    con.row_factory = sqlite3.Row
    cur = con.execute("select * from x where id > ?", [1])
    for row in cur:
        print(row["id"], row["x"])
