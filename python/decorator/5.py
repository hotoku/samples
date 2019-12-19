# 4.pyの続き


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

# デコレートされる関数とデコレートによって作成される関数でオブジェクトを共有しないといけない
# ということが問題の根元ぽいことが分かった
# そこで、両者の変数の名前解決のルートに共有したいオブジェクトを置いてあげれば問題が解決しそう
# グローバルにおけば解決といえば解決だけど、自明なので、その案は却下
# あるいはモジュール化すれば、パッケージの名前空間を使えるから、それもアリだが、今は１ファイルのスクリプトで使いたいので
# クラスによる実装を考える
# クラスによる実装とした場合、各関数をメンバー関数にするかclassmethodにするかstaticmethodにするかの選択肢がある
# メンバー関数 or classmethodにすると、self or clsで共通の要素にアクセスできて良さそうな気がする
# と思いきや、メンバー関数だと関数定義の時点ではselfが存在しないので無理ぽい


# class DB:
#     def __init__(self):
#         self.con = sqlite.connect()

#     def transaction(self, f):
#         self.cur = self.con.cursor()

#     @transaction
#     def execute(self, sql):
#         self.cur.execute(sql)


# こんな感じに書きたいけど、executeの定義時にはselfはないので厳しそう
# staticmethodで試してみる


# class DB2:
#     con = sqlite3.connect(":memory:")
#     cur = None

#     @classmethod
#     def transaction(cls, query_func):
#         def execute(*args, **kwargs):
#             cls.cur = cls.con.connect()
#             try:
#                 ret = query_func(*args, **kwargs)
#                 cls.cur.commit()
#                 return ret
#             except Exception as e:
#                 cls.con.rollback()
#                 raise e
#             finally:
#                 cls.cur.close()

#     @classmethod
#     @transaction
#     def execute(cls, sql):
#         return cls.cur.execute(sql)

#     @classmethod
#     @transaction
#     def executemany(cls, sql, it):
#         return cls.cur.executemany(sql, it)

#     @classmethod
#     @transaction
#     def executescript(cls, sql):
#         return cls.cur.executescript(sql)


# DB2.execute("sql")
# DB2.executemany("sql", "it")
# DB2.executescript("sql")

# これだと
# @transaction
# TypeError: 'classmethod' object is not callable
# というエラーになる。これは意味が分からない・・

# 直接↑の理由とは関係ないが、よく考えると、transactionは、DB2.transactionという形で呼ばないといけないはず
# executeの定義の段階ではDB2はまだできてないので、上の方法だと無理ぽ
