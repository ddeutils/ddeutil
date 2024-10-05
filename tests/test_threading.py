import time
from functools import partial

from ddeutil.core.threader import MonitorThread


def log_override(msg: str, keeping: list) -> None:  # pragma: no cove
    keeping.append(msg)
    print(msg)


def test_monitoring_thread():
    keeps: list[str] = []

    thread = MonitorThread(
        log=partial(log_override, keeping=keeps),
        waiting=2,
    )
    thread.start()

    time.sleep(4.5)

    thread.stop()

    assert 2 <= len(keeps) < 4