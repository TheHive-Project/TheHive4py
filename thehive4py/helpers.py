import datetime as dt


def dt_to_ts(datetime: dt.datetime) -> int:
    """Convert datetime object to TheHive timestamp."""
    return int(datetime.timestamp() * 1000)


def ts_to_dt(timestamp: int, tz: dt.timezone = None) -> dt.datetime:
    """Convert TheHive timestamp to datetime object."""
    return dt.datetime.fromtimestamp(timestamp / 1000.0, tz=tz)
