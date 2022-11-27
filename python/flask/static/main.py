"""静的ファイルの送信の例

## `Flask`の`static_folder`引数にフォルダパスを指定する。

この場合、そのフォルダ以下のファイルへのrouteが自動で登録される。

このファイルでは、`static_folder="./static"`が指定されている。
これによって、`GET /static/js/main.js`というリクエストに対して
`./static/js/main.js`というファイルが返答される。

## `send_file`を使う

`send_file`を使えば、任意のファイルを返答することができる。
"""

from flask import Flask, send_file

app = Flask(
    "sample",
    static_folder="./static"
)


@app.route("/")
def index():
    return send_file("./index.html")


@app.route("/<string:file>")
def root_file(file: str):
    print(f"{file=}")
    return send_file(f"./{file}")


@app.route("/<path:path>")
def any(path: str):
    print(f"{path=}")
    return send_file("./index.html")


def main():
    app.run(port=12346, debug=True)


if __name__ == "__main__":
    main()
