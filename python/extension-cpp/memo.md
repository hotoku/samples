## エラーと例外

関数が処理に失敗した場合の挙動。

- 例外状態をセット
- エラーを示す値（通常はNULLポインタ）を返す

例外を管理する3つのグローバル変数がある。

- 例外の値それ自身。NULLなら例外は起こってないとみなされる。
- 例外の付属値（raiseの第2引数）
- エラーの発生源がPythonコード内だった場合にスタックトレースを置いておくところ

例外をセットする関数たち

- `PyErr_SetString`: 引数は例外オブジェクトとC文字列
- `PyErr_SetFromErrno`: 引数は例外のみ。付属値はerrnoから自動で作られる
- `PyErr_SetObject`: 最も汎用的

例外がセットされているかどうか？`PyErr_Occured`で調べる。


fの中でgが呼ばれているときに、gが失敗した場合、fはエラー値（NULL）を返すべきだが、
PyErr*を呼ぶ必要はない（gの中で呼ばれているから）。fがPyErrを呼ぶことも可能ではあるが、
事情がなければ辞めた方が良い。

`PyError_Clear`で、例外を消すことができる。Pythonインタプリタに例外を渡さずに処理する場合は使う。

malloc/reallocを直接、自分で呼び出す関数は、それらが失敗した時には必ずPyErr_NoMemoryを呼び出す。

返り値：整数のステータスコードを返す関数は、0 or 正の値を成功、-1を失敗とみなす。ただし、PyArg_ParseTupleは例外。

ごみ処理：エラーを返す時には、`Py_XDECREF`や`Py_DECREF`を呼び出して、ごみ処理を確実に行うこと。

どの例外を返すかは自由に選べる。

組み込み例外は、対象となるオブジェクトが用意されている。そうでない場合、自分で定義することもできる。




## 例

```
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    if (sts < 0) {
        PyErr_SetString(SpamError, "System command failed");
        return NULL;
    }
    return PyLong_FromLong(sts);
}
```


`PyArg_ParseTuple`は引数を解析するための関数。
2番目の引数が型を示すテンプレート。`command`は、結果を保存するためのポインタ。
`PyArg_ParseTuple`が失敗した場合は、その中で例外処理が行われているので単純にNULLを返す。

`sts`が負の場合は、自分で例外状態をセットしてNULLを返す。

最後に、long型の値をPythonのオブジェクトに変換して返す。


## メソッドテーブル

自作の関数は「メソッドテーブル」で管理される。

```
static PyMethodDef SpamMethods[] = {
    ...
    {"system",  spam_system, METH_VARARGS,
     "Execute a shell command."},
    ...
    {NULL, NULL, 0, NULL}        /* Sentinel */
};
```


`METH_VARARGS`は、関数が位置引数だけを使うことを示している。
キーワード引数も使う場合は`METH_VARARGS | METH_KEYWORDS`を使う。
最後の要素は、番兵(sentinel)?。


`METH_KEYWORDS`を使うときには、関数は3つ目の引数として`PyObject*`を
受け取るようにしておく。ここに、辞書オブジェクトが渡される。
この引数は`PyArg_ParseTupleAndKeywords`で解釈できる。

メソッドテーブルは、モジュールを定義する構造体に渡される。

```
static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",   /* name of module */
    spam_doc, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    SpamMethods
};
```

さらに、この構造体は、モジュールの初期化関数内でインタプリタに渡される。

```
PyMODINIT_FUNC
PyInit_spam(void){
    return PyModule_Create(&spammodule);
}
```

モジュールの初期化関数は`PyInit_<module名>`という形式出ないとダメ。

## ビルド

C拡張の実体は共有ライブラリ（.soファイル）。いくつかの制約がある。

- ファイルはPYTHONPATH上になくてはならない。
- ファイル名はモジュール名でなくてはならない。
- 拡張子は.soでないとだめ

ライブラリの中に、`PyObject* PyInit_<モジュール名>`という関数がないとだめ。

## setup.py

```
from distutils.core import setup, Extension

module1 = Extension('demo',
                    sources = ['demo.c'])

setup (name = 'PackageName',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
```
こういう`setup.py`を作って、`python setup.py build`を実行すれば、soができる、らしい。
