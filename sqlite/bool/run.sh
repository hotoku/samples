#!/bin/bash


if ! [[ -f db.sqlite ]]; then
    cat<<EOF  | sqlite3 db.sqlite
create table bools (
       name text not null,
       bool interger nullable
);
insert into bools (name, bool) values ("1", 1);
insert into bools (name, bool) values ("0", 0);
insert into bools (name, bool) values ("NULL", NULL);
insert into bools (name, bool) values ("TRUE", TRUE);
insert into bools (name, bool) values ("FALSE", FALSE);
EOF
fi


echo "--"
echo "select * from bools where bool" | sqlite3 db.sqlite

echo "--"
echo "select * from bools where not bool" | sqlite3 db.sqlite

echo "--"
echo "select * from bools where bool = TRUE" | sqlite3 db.sqlite

echo "--"
echo "select * from bools where bool = FALSE" | sqlite3 db.sqlite

# --
# 1|1
# TRUE|1
# --
# 0|0
# FALSE|0
# --
# 1|1
# TRUE|1
# --
# 0|0
# FALSE|0
