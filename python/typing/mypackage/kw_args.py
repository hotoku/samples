from typing import Dict, Any


def f(**kw_args: Dict[str, Any]):
    # これは型エラー
    # 上のように型注釈すると、kw_args: Dict[str, Dict[str, Any]]と解釈されるらしい
    x: int = kw_args["a"]
    print(x)


def g(**kw_args: Dict[str, Any]):
    x: int = kw_args["a"]
    print(x)
