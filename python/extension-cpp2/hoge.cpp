#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <cmath>

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

static PyMethodDef HogeMethods[] = {
  {
    "func",
    hoge_func,
    METH_VARARGS,
    "calculate norms"
  },
  {NULL, NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef hogemodule = {
  PyModuleDef_HEAD_INIT,
  "hoge",          /* name of module */
  "sample module", /* module documentation, may be NULL */
  -1,              /* size of per-interpreter state of the module,
                      or -1 if the module keeps state in global variables. */
  HogeMethods
};


PyMODINIT_FUNC
PyInit_hoge(void){
  return PyModule_Create(&hogemodule);
}



// Local Variables:
// flycheck-gcc-include-path: ("/usr/local/anaconda3/include/python3.8")
// flycheck-clang-include-path: ("/usr/local/anaconda3/include/python3.8")
// End:
