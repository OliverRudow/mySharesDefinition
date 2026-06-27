"""myCalendarWatchListDefinitions.py."""

__title__: str = "myCalendarWatchListDefinitions"
__version__: str = "0.3.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from mydatabase.mySQLDataBase import STR_SQL_DATA_BASE_NAME, STR_SQL_DATA_DIR_NAME
from mytuple import myTuple

def init_dict_calendar_watch_list_data() -> dict[str,  str | int | None]:
    elem = 0

    for key in DICT_STATIC_WATCH_LIST_DATA:
        DICT_STATIC_WATCH_LIST_DATA[key] = EMPTY_LIST_ENTIRE_ROW[elem]
        elem += 1

    return DICT_STATIC_WATCH_LIST_DATA

STR_DATA_BASE_FILE_NAME: str = STR_SQL_DATA_BASE_NAME

STR_DATA_BASE_DIR_NAME: str = STR_SQL_DATA_DIR_NAME

STR_DATA_BASE_TABLE_NAME: str = 'calendar_watch_list'

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 5.0

DATA_BASE_CONNECTION_URI: bool = True

DATA_BASE_FLAG_ADD_DATE: bool = False

DATA_BASE_FLAG_CLEAN_PRECEDED_DATA: bool = False

DATA_BASE_INT_NUMBER_PRECEDED_DATA = 0

LIST_SECTIONS_WATCH_LIST: list[str] = ['CALENDAR_WATCH_LIST.QUOTE_ISIN',
                                       'CALENDAR_WATCH_LIST.DIVIDEND_DATE',
                                       'CALENDAR_WATCH_LIST.DIVIDEND_DELTA_DATE',
                                       'CALENDAR_WATCH_LIST.EX_DIVIDEND_DATE',
                                       'CALENDAR_WATCH_LIST.EX_DIVIDEND_DELTA_DATE',
                                       'CALENDAR_WATCH_LIST.EARNINGS_DATE',
                                       'CALENDAR_WATCH_LIST.EARNINGS_DELTA_DATE',
                                       ]

TUPLE_CALENDAR_WATCH_LIST_QUOTE_ISIN: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('CALENDAR_WATCH_LIST.QUOTE_ISIN',
    'quote_isin',
    ('quote_isin', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_CALENDAR_WATCH_LIST_DIVIDEND_DATE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('CALENDAR_WATCH_LIST.DIVIDEND_DATE',
    'dividend_date',
    ('dividend_date', 'TEXT'),
    tuple)

TUPLE_CALENDAR_WATCH_LIST_DIVIDEND_DELTA_DATE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('CALENDAR_WATCH_LIST.DIVIDEND_DELTA_DATE',
    'dividend_delta_date',
    ('dividend_delta_date', 'INTEGER'),
    tuple)

TUPLE_CALENDAR_WATCH_LIST_EX_DIVIDEND_DATE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('CALENDAR_WATCH_LIST.EX_DIVIDEND_DATE',
    'ex_dividend_date',
    ('ex_dividend_date', 'TEXT'),
    tuple)

TUPLE_CALENDAR_WATCH_LIST_EX_DIVIDEND_DELTA_DATE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('CALENDAR_WATCH_LIST.EX_DIVIDEND_DELTA_DATE',
    'ex_dividend_delta_date',
    ('ex_dividend_delta_date', 'INTEGER'),
    tuple)

TUPLE_CALENDAR_WATCH_LIST_EARNINGS_DATE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('CALENDAR_WATCH_LIST.EARNINGS_DATE',
    'earnings_date',
    ('earnings_date', 'TEXT'),
    tuple)

TUPLE_CALENDAR_WATCH_LIST_EARNINGS_DELTA_DATE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('CALENDAR_WATCH_LIST.EARNINGS_DELTA_DATE',
    'earnings_delta_date',
    ('earnings_delta_date', 'INTEGER'),
    tuple)

_index_tuple = myTuple.MyTuple

LIST_CALENDAR_WATCH_LIST_COLUMN_NAMES: list[str] = [TUPLE_CALENDAR_WATCH_LIST_QUOTE_ISIN[
                                                      _index_tuple.OPTION_NAME],
                                                   TUPLE_CALENDAR_WATCH_LIST_DIVIDEND_DATE[
                                                      _index_tuple.OPTION_NAME],
                                                   TUPLE_CALENDAR_WATCH_LIST_DIVIDEND_DELTA_DATE[
                                                      _index_tuple.OPTION_NAME],
                                                   TUPLE_CALENDAR_WATCH_LIST_EX_DIVIDEND_DATE[
                                                      _index_tuple.OPTION_NAME],
                                                   TUPLE_CALENDAR_WATCH_LIST_EX_DIVIDEND_DELTA_DATE[
                                                      _index_tuple.OPTION_NAME],
                                                   TUPLE_CALENDAR_WATCH_LIST_EARNINGS_DATE[
                                                      _index_tuple.OPTION_NAME],
                                                   TUPLE_CALENDAR_WATCH_LIST_EARNINGS_DELTA_DATE[
                                                      _index_tuple.OPTION_NAME],]

DICT_STATIC_WATCH_LIST_DATA: dict[str,  str | int | None] = dict.fromkeys(LIST_CALENDAR_WATCH_LIST_COLUMN_NAMES)

EMPTY_LIST_ENTIRE_ROW: list = ['', '', '', '', '', '', '']

INDEX_PRIMARY_KEY = LIST_CALENDAR_WATCH_LIST_COLUMN_NAMES.index(TUPLE_CALENDAR_WATCH_LIST_QUOTE_ISIN[
                                                      _index_tuple.OPTION_NAME])
