"""myCalendarWatchListDefinitions.py."""

__title__: str = "myCalendarWatchListDefinitions"
__version__: str = "0.3.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from mydatabase.mySQLDataBase import STR_SQL_DATA_BASE_NAME, STR_SQL_DATA_DIR_NAME
from mytuple import myTuple

def init_dict_static_watch_list_data() -> dict[str, str| bool | None]:
    elem = 0

    for key in DICT_STATIC_WATCH_LIST_DATA:
        DICT_STATIC_WATCH_LIST_DATA[key] = EMPTY_LIST_ENTIRE_ROW[elem]
        elem += 1

    return DICT_STATIC_WATCH_LIST_DATA

STR_DATA_BASE_FILE_NAME: str = STR_SQL_DATA_BASE_NAME

STR_DATA_BASE_DIR_NAME: str = STR_SQL_DATA_DIR_NAME

STR_DATA_BASE_TABLE_NAME: str = 'static_watch_list'

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 5.0

DATA_BASE_CONNECTION_URI: bool = True

LIST_SECTIONS_WATCH_LIST: list[str] = ['STATIC_WATCH_LIST.QUOTE_NAME',
                                       'STATIC_WATCH_LIST.QUOTE_TYPE',
                                       'STATIC_WATCH_LIST.QUOTE_ISIN',
                                       'STATIC_WATCH_LIST.QUOTE_WKN',
                                       'STATIC_WATCH_LIST.QUOTE_TICKER_SYMBOL',
                                       'STATIC_WATCH_LIST.QUOTE_INDUSTRY',
                                       'STATIC_WATCH_LIST.QUOTE_SECTOR',
                                       'STATIC_WATCH_LIST.QUOTE_CURRENCY',
                                       'STATIC_WATCH_LIST.QUOTE_INVEST_STATUS']

TUPLE_STATIC_WATCH_LIST_QUOTE_NAME: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('STATIC_WATCH_LIST.QUOTE_NAME',
    'quote_name',
    ('quote_name', 'TEXT'),
    tuple)

TUPLE_STATIC_WATCH_LIST_QUOTE_TYPE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('STATIC_WATCH_LIST.QUOTE_TYPE',
     'quote_type',
    ('quote_type', 'TEXT'),
    tuple)

TUPLE_STATIC_WATCH_LIST_QUOTE_ISIN: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('STATIC_WATCH_LIST.QUOTE_ISIN',
     'quote_isin',
    ('quote_isin', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_STATIC_WATCH_LIST_QUOTE_TICKER_SYMBOL: tuple[str, str, tuple[str, str, str], type[tuple]] = \
    ('STATIC_WATCH_LIST.QUOTE_TICKER_SYMBOL',
     'quote_ticker_symbol',
    ('quote_ticker_symbol', 'TEXT', 'NOT NULL'),
    tuple)

TUPLE_STATIC_WATCH_LIST_QUOTE_INDUSTRY: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('STATIC_WATCH_LIST.QUOTE_INDUSTRY',
     'quote_industry',
    ('quote_industry', 'TEXT'),
     tuple)

TUPLE_STATIC_WATCH_LIST_QUOTE_SECTOR: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('STATIC_WATCH_LIST.QUOTE_SECTOR',
     'quote_sector',
    ('quote_sector', 'TEXT'),
     tuple)

TUPLE_STATIC_WATCH_LIST_QUOTE_CURRENCY: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('STATIC_WATCH_LIST.QUOTE_CURRENCY',
    'quote_currency',
    ('quote_currency', 'TEXT'),
     tuple)

TUPLE_STATIC_WATCH_LIST_QUOTE_INVEST_STATUS: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('STATIC_WATCH_LIST.QUOTE_INVEST_STATUS',
    'invest_status',
    ('invest_status', 'BIT'),
    tuple)


LIST_STATIC_WATCH_LIST_FILTER_OPTIONS: list[tuple] = [TUPLE_STATIC_WATCH_LIST_QUOTE_NAME,
                                                      TUPLE_STATIC_WATCH_LIST_QUOTE_TYPE,
                                                      TUPLE_STATIC_WATCH_LIST_QUOTE_ISIN,
                                                      TUPLE_STATIC_WATCH_LIST_QUOTE_TICKER_SYMBOL,
                                                      TUPLE_STATIC_WATCH_LIST_QUOTE_INDUSTRY,
                                                      TUPLE_STATIC_WATCH_LIST_QUOTE_SECTOR,
                                                      TUPLE_STATIC_WATCH_LIST_QUOTE_CURRENCY,
                                                      TUPLE_STATIC_WATCH_LIST_QUOTE_INVEST_STATUS]

_index_tuple = myTuple.MyTuple

LIST_STATIC_WATCH_LIST_COLUMN_NAMES: list[str] = [TUPLE_STATIC_WATCH_LIST_QUOTE_NAME[
                                                      _index_tuple.OPTION_NAME],
                                                  TUPLE_STATIC_WATCH_LIST_QUOTE_TYPE[
                                                      _index_tuple.OPTION_NAME],
                                                  TUPLE_STATIC_WATCH_LIST_QUOTE_ISIN[
                                                      _index_tuple.OPTION_NAME],
                                                  TUPLE_STATIC_WATCH_LIST_QUOTE_TICKER_SYMBOL[
                                                      _index_tuple.OPTION_NAME],
                                                  TUPLE_STATIC_WATCH_LIST_QUOTE_INDUSTRY[
                                                      _index_tuple.OPTION_NAME],
                                                  TUPLE_STATIC_WATCH_LIST_QUOTE_SECTOR[
                                                      _index_tuple.OPTION_NAME],
                                                  TUPLE_STATIC_WATCH_LIST_QUOTE_CURRENCY[
                                                      _index_tuple.OPTION_NAME],
                                                  TUPLE_STATIC_WATCH_LIST_QUOTE_INVEST_STATUS[
                                                      _index_tuple.OPTION_NAME]]

DICT_STATIC_WATCH_LIST_DATA: dict[str, str | bool | None] = dict.fromkeys(LIST_STATIC_WATCH_LIST_COLUMN_NAMES)

EMPTY_LIST_ENTIRE_ROW: list = ['', '', '', '', '', '', '', False]

INDEX_PRIMARY_KEY = LIST_STATIC_WATCH_LIST_COLUMN_NAMES.index(TUPLE_STATIC_WATCH_LIST_QUOTE_ISIN[
                                                      _index_tuple.OPTION_NAME])
