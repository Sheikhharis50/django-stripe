from datetime import datetime


def readable_date(date: datetime, format="%Y-%m-%d %H:%M:%S"):
    return date.strftime(format)
