import datetime as dt
import time


def now_to_ts() -> int:
    """Return now as TheHive timestamp."""
    return int(time.time() * 1000)


def dt_to_ts(datetime: dt.datetime) -> int:
    """Convert datetime object to TheHive timestamp."""
    return int(datetime.timestamp() * 1000)


def ts_to_dt(timestamp: int, tz: dt.timezone = None) -> dt.datetime:
    """Convert TheHive timestamp to datetime object."""
    return dt.datetime.fromtimestamp(timestamp / 1000.0, tz=tz)
