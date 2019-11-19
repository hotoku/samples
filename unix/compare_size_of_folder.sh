#!/bin/bash

## stat -f"フォーマット"で、欲しい情報だけ出せる
## %N: ファイル名
## %Z: サイズ
diff -u <(cd epilogue; stat -f"%N %Z" *) <(cd epilogue0923; stat -f"%N %Z" *)
