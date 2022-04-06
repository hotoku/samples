import pytest
from xprocess import ProcessStarter


@pytest.fixture
def hoge(xprocess):
    port = 8080

    class Starter(ProcessStarter):
        pattern = r"server start"  # type: ignore
        timeout = 1
        terminate_on_interrupt = True
        args = [  # type: ignore
            "python", "/home/hotoku/projects/hotoku/samples/python/pytest-xprocess/server.py"]
    logfile = xprocess.ensure("myserver", Starter)
    # logfileは、PIDと、ログファイルのパス
    # ログファイルは、.pytest_cache/d/.xprocess 以下にあるぽい

    yield dict(port=port, logfile=logfile)

    xprocess.getinfo("myserver").terminate()
