#!/bin/bash

if ! [[ -f db.sqlite ]]; then
    cat<<EOF  | sqlite3 db.sqlite
create table clients (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name text not null
);

insert into clients (name) values ("client1");

create table deals (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       client_id integer not null,
       name text not null,
       foreign key(client_id) references clients(id)
);

insert into deals (name, client_id) values ("deal1", 1);

EOF
fi

## これは失敗する
## ※ PRAGMAが必要
# cat<<EOF | sqlite3 db.sqlite
# PRAGMA foreign_keys = ON;
# insert into deals (client_id, name)
# values (2, "deal2")
# EOF

## これは失敗する
## ※ PRAGMAが必要
# cat<<EOF | sqlite3 db.sqlite
# PRAGMA foreign_keys = ON;
# delete from clients
# where id=1
# EOF

## 順番に消せば成功する
cat <<EOF | sqlite3 db.sqlite
delete from deals where id=1;
delete from clients where id=1;
EOF
