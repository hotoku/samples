#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <cmath>
#include <iostream>

using namespace std;

struct norms {
  double one;
  double two;
};

norms func(const double& x, const double& y){
  return {
    abs(x) + abs(y),
    sqrt(x*x + y*y)
  };
}

#ifdef HOTOKU_DEBUG

int main(){
  auto ret = func(1, 2);
  cout << ret.one << "," << ret.two << endl;
}

#else

static PyObject* hoge_func(PyObject *self, PyObject *args){
  double x, y;

  if (!PyArg_ParseTuple(args, "dd", &x, &y))
    return NULL;
  norms vals = func(x, y);
  PyObject* ret = PyList_New(0);
  PyObject* p;
  p = PyFloat_FromDouble(vals.one);
  PyList_Append(ret, p);
  p = PyFloat_FromDouble(vals.two);
  PyList_Append(ret, p);
  return ret;
}

// 関数情報のリスト
static PyMethodDef HogeMethods[] = {
  {
    "func",           // Pythonから見える関数名
    hoge_func,        // 関数の実体
    METH_VARARGS,     // 引数のタイプ
    "calculate norms" // ドキュメント
  },
  {NULL, NULL, 0, NULL} /* Sentinel */
};

// モジュールの情報
static struct PyModuleDef hogemodule = {
  PyModuleDef_HEAD_INIT,
  "hoge",          // モジュール名
  "sample module", // ドキュメント
  -1,              // -1固定（詳細を調べてない）
  HogeMethods      // 上で定義した関数のリスト
};


/* モジュールの定義
   1. PyMODINIT_FUNCを付ける
   2. PyInit_<モジュール名> という命名規約に従う
*/
PyMODINIT_FUNC
PyInit_hoge(void){
  return PyModule_Create(&hogemodule); // 上で定義したモジュール情報を渡す
}

#endif

// Local Variables:
// flycheck-gcc-include-path: ("/usr/local/anaconda3/include/python3.8")
// flycheck-clang-include-path: ("/usr/local/anaconda3/include/python3.8")
// End:
