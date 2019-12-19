# transaction用のdecoratorを実現できるか？


# サンプル用のダミークラスたち
class Sqlite3:
    def connect(self, s):
        print(f"connect: {s}")
        return Connection()


class Connection:
    def cursor(self):
        print("cursor")
        return Cursor()

    def close(self):
        print("close")

    def rollback(self):
        print("rollback")

    def commit(self):
        print("commit")


class Cursor:
    def execute(self, sql):
        print(f"execute: {sql}")

    def executemany(self, sql, it):
        print(f"executemany: {sql} {it}")

    def executescript(self, sql):
        raise Exception("panic")


sqlite3 = Sqlite3()


# デコレータを使わない例
def myexecute(sql):
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except Exception:
        con.rollback()
    finally:
        con.close()


def myexecutemany(sql, it):
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    try:
        cur.executemany(sql, it)
        con.commit()
    except Exception:
        con.rollback()
    finally:
        con.close()


# 上の２つの関数はほとんど同じコードなのでデコレータでまとめたい
# ２つの関数で異なっている部分をデコレータの引数に機械的に置き換えると
# こんな感じになるが・・
# curはoriginalなど持っていないので、うまくいかない
# def deco1(original):
#     def defined(sql):
#         con = sqlite3.connect(":memory:")
#         cur = con.cursor()
#         try:
#             ret = cur.original(sql)
#             con.commit()
#         except Exception:
#             con.rollback()
#         finally:
#             con.close()
#         return ret
#     return defined


# そもそも、最終的に実現したいコードは、どういう見た目になるのか？
# こんな感じか・・？
# @deco
# def myexecute(con, sql):
#     cur = con.cursor()
#     cur.execute(sql)

# 難しさの根元の部分をうまく言語化したい
# 問題っぽいところ：
# - con, curというオブジェクトが、myexecuteの中でも外でも使われている
# - con, curというオブジェクトは、関数定義時ではなくて関数呼出時に初期化されて欲しい

# 考察：
# 関数の呼出時に実行されるコードは、definedの内側のコード
# con, curは、definedの中で初期化されなければならない
# ということは、con, curをdefinedの中で初期化した後に、originalに渡してやれば動く・・？


def deco2(original):
    def defined(*args, **kwargs):
        con = sqlite3.connect(":memory:")
        cur = con.cursor()
        try:
            ret = original(cur, *args, **kwargs)
            con.commit()
            return ret
        except Exception as e:
            con.rollback()
            raise e
        finally:
            con.close()
    return defined


@deco2
def myexecute(cur, sql):
    return cur.execute(sql)


@deco2
def myexecutemany(cur, sql, it):
    return cur.executemany(sql, it)


@deco2
def myexecutescript(cur, sql):
    return cur.executescript(sql)

# 動作を検証してみよう


myexecute("sql")
myexecutemany("sql", "it")
myexecutescript("sql")


# 期待した動作にはなるが、定義時のシグネチャと実行時のシグネチャが異なってしまう・・
# curは、definedの中で初期化されなければならない。かつ、originalの中でも使われる。
# ということは、definedの名前解決パスとoriginalの名前解決パスの共通部分にcon, curがあれば、欲しい動作にできる気がする
