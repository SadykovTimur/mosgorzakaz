from datetime import datetime

__all__ = ['today', 'normalize']


def today() -> datetime:
    return datetime.today().replace(second=0, microsecond=0)


def normalize(date_str: str, date_format: str = '%d.%m.%Y %H:%M') -> datetime:
    return datetime.strptime(date_str, date_format)
