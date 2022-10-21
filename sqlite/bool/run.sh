#!/bin/bash


if ! [[ -f db.sqlite ]]; then
    cat<<EOF  | sqlite3 db.sqlite
create table bools (
       name text not null,
       bool interger nullable
);
insert into bools (name, bool) values ("TRUE", 1);
insert into bools (name, bool) values ("FALSE", 0);
insert into bools (name, bool) values ("NULL", NULL);
EOF
fi


echo "select * from bools where bool" | sqlite3 db.sqlite
# => TRUE|1


echo "select count(1) from bools where bool" | sqlite3 db.sqlite
# => 1
