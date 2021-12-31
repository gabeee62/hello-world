import datetime

date = datetime.datetime.now()


def get_year():
    return date.year


def get_month():
    return date.month


def get_day():
    return date.day


def get_hour():
    return date.hour


def get_min():
    return date.minute


def get_sec():
    return date.second


def get_micro():
    return date.microsecond
