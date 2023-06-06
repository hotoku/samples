# アプリのログはinfoで出したいが外部ライブラリはwarnだけで良い、などの場合には、ロガーごとにレベルを変えたい

import logging
import sys


# rootのレベルはデフォルトでwarning
root = logging.getLogger()

# 独自にインスタンス化するロガーも、デフォルトのレベルはwarning
LOGGER1 = logging.getLogger(__name__ + "1")
LOGGER2 = logging.getLogger(__name__ + "2")

# LOGGER1のレベルをINFOに変更
LOGGER1.setLevel(logging.INFO)

# レベルを変更するだけでは、infoログは表示されない。
# LOGGER1.infoでレコードは作成されるが、ハンドラが設定されていないため、rootロガーに送られる。
# rootロガーのレベルはwarningのため、レコードは破棄される。
LOGGER1.info("info 1")
LOGGER1.warning("warning 1")

LOGGER2.info("info 2")
LOGGER2.warning("warning 2")

# LOGGER1にだけ、独自のハンドラを追加する。
handler = logging.StreamHandler(sys.stderr)
LOGGER1.addHandler(handler)

LOGGER1.info("2nd info 1")
LOGGER1.warning("2nd warning 1")

LOGGER2.info("2nd info 2")
LOGGER2.warning("2nd warning 2")
