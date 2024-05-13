from datetime import datetime as dt


def _format_time(arrival_time):
    return dt.strptime(arrival_time, "%H:%M:%S").time()
