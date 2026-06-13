"""myReportTopListDefinitions.py."""

__title__: str = "myReportTopListDefinitions"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from data_base_me.mySQLDataBase import STR_SQL_DATA_BASE_NAME, STR_SQL_DATA_DIR_NAME
from watchlist_definition_me import myStaticWatchListDefinitions
from watchlist_definition_me import myPerformanceWatchListDefinitions
from watchlist_definition_me import myRankingWatchListDefinitions
from tuple_me import myTuple


STR_DATA_BASE_FILE_NAME: str = STR_SQL_DATA_BASE_NAME

STR_DATA_BASE_DIR_NAME: str = STR_SQL_DATA_DIR_NAME

STR_DATA_BASE_TABLE_NAME: str = 'report_top_list'

STR_DATA_BASE_TABLE_NAME_STATIC: str = myStaticWatchListDefinitions.STR_DATA_BASE_TABLE_NAME

STR_DATA_BASE_TABLE_NAME_PERFORMANCE: str = myPerformanceWatchListDefinitions.STR_DATA_BASE_TABLE_NAME

STR_DATA_BASE_TABLE_NAME_RANKING: str = myRankingWatchListDefinitions.STR_DATA_BASE_TABLE_NAME

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 10.0

DATA_BASE_CONNECTION_URI: bool = True

LIST_SECTIONS_WATCH_LIST: list[str] = ['TUPLE_REPORT_TOP_LIST_QUOTE_ISIN',
                                       'TUPLE_REPORT_TOP_LIST_QUOTE_NAME',
                                       'TUPLE_REPORT_TOP_LIST_QUOTE_INDUSTRY',
                                       'TUPLE_REPORT_TOP_LIST_QUOTE_CURRENCY',
                                       'TUPLE_REPORT_TOP_LIST_CURRENT_PRICE',
                                       'TUPLE_REPORT_TOP_LIST_CHANGE_PERCENT',
                                       'TUPLE_REPORT_TOP_LIST_CHANGE_PERCENT_TWENTY_DAY',
                                       'TUPLE_REPORT_TOP_LIST_ANALYST_SCORE',
                                       'TUPLE_REPORT_TOP_LIST_DERIVATE_SCORE',
                                       'TUPLE_REPORT_TOP_LIST_FUNDAMENTALS_SCORE',
                                       'TUPLE_REPORT_TOP_LIST_PERFORMANCE_SCORE',
                                       'TUPLE_REPORT_TOP_LIST_TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY',
                                       'TUPLE_REPORT_TOP_LIST_OVERALL_SCORE',
                                       'TUPLE_REPORT_TOP_LIST_SHIFT',]

TUPLE_REPORT_TOP_LIST_QUOTE_ISIN: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('REPORT_TOP_LIST.QUOTE_ISIN',
     'isin',
    ('isin', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_REPORT_TOP_LIST_QUOTE_NAME: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('REPORT_TOP_LIST.QUOTE_NAME',
    'name',
    ('name', 'TEXT'),
    tuple)

TUPLE_REPORT_TOP_LIST_QUOTE_INDUSTRY: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('REPORT_TOP_LIST.QUOTE_INDUSTRY',
     'industry',
    ('industry', 'TEXT'),
     tuple)

TUPLE_REPORT_TOP_LIST_QUOTE_CURRENCY: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('REPORT_TOP_LIST.QUOTE_CURRENCY',
    'ccy',
    ('ccy', 'TEXT'),
     tuple)

TUPLE_REPORT_TOP_LIST_CURRENT_PRICE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('REPORT_TOP_LIST.CURRENT_PRICE',
    'price',
    ('price', 'REAL'),
    tuple)

TUPLE_REPORT_TOP_LIST_CHANGE_PERCENT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('REPORT_TOP_LIST.REGULAR_MARKET_CHANGE_PERCENT',
    '"%"',
    ('"%"', 'REAL'),
    tuple)

TUPLE_REPORT_TOP_LIST_CHANGE_PERCENT_TWENTY_DAY: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('REPORT_TOP_LIST.REGULAR_MARKET_CHANGE_PERCENT_TWENTY_DAY',
    '"%_20d"',
    ('"%_20d"', 'REAL'),
    tuple)

TUPLE_REPORT_TOP_LIST_ANALYST_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('REPORT_TOP_LIST.ANALYST_SCORE',
     'aly_sc',
    ('aly_sc', 'REAL'),
    tuple)

TUPLE_REPORT_TOP_LIST_DERIVATE_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('REPORT_TOP_LIST.DERIVATE_SCORE',
     'der_sc',
    ('der_sc', 'REAL'),
    tuple)

TUPLE_REPORT_TOP_LIST_FUNDAMENTALS_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('REPORT_TOP_LIST.FUNDAMENTALS_SCORE',
     'fdm_sc',
    ('fdm_sc', 'REAL'),
    tuple)

TUPLE_REPORT_TOP_LIST_PERFORMANCE_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('REPORT_TOP_LIST.PERFORMANCE_SCORE',
     'perf_sc',
    ('perf_sc', 'REAL'),
    tuple)

TUPLE_REPORT_TOP_LIST_TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('REPORT_TOP_LIST.TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY',
    'twenty_d_cp_array',
    ('twenty_d_cp_array', 'BLOB'),
    tuple)

TUPLE_REPORT_TOP_LIST_OVERALL_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('REPORT_TOP_LIST.OVERALL_SCORE',
     'score',
    ('score', 'REAL'),
    tuple)

TUPLE_REPORT_TOP_LIST_SHIFT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('REPORT_TOP_LIST.SHIFT',
     'shift',
    ('shift', 'INTEGER'),
    tuple)

_index_tuple = myTuple.MyTuple

LIST_REPORT_TOP_LIST_COLUMN_NAMES: list[str] = [TUPLE_REPORT_TOP_LIST_QUOTE_ISIN[
                                                      _index_tuple.OPTION_NAME],
                                                TUPLE_REPORT_TOP_LIST_QUOTE_NAME[
                                                      _index_tuple.OPTION_NAME],
                                                TUPLE_REPORT_TOP_LIST_QUOTE_INDUSTRY[
                                                      _index_tuple.OPTION_NAME],
                                                TUPLE_REPORT_TOP_LIST_QUOTE_CURRENCY[
                                                      _index_tuple.OPTION_NAME],
                                                TUPLE_REPORT_TOP_LIST_CURRENT_PRICE[
                                                      _index_tuple.OPTION_NAME],
                                                TUPLE_REPORT_TOP_LIST_CHANGE_PERCENT[
                                                      _index_tuple.OPTION_NAME],
                                                TUPLE_REPORT_TOP_LIST_CHANGE_PERCENT_TWENTY_DAY[
                                                      _index_tuple.OPTION_NAME],
                                                TUPLE_REPORT_TOP_LIST_ANALYST_SCORE[
                                                      _index_tuple.OPTION_NAME],
                                                TUPLE_REPORT_TOP_LIST_DERIVATE_SCORE[
                                                    _index_tuple.OPTION_NAME],
                                                TUPLE_REPORT_TOP_LIST_FUNDAMENTALS_SCORE[
                                                    _index_tuple.OPTION_NAME],
                                                TUPLE_REPORT_TOP_LIST_PERFORMANCE_SCORE[
                                                    _index_tuple.OPTION_NAME],
                                                TUPLE_REPORT_TOP_LIST_TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY[
                                                    _index_tuple.OPTION_NAME],
                                                TUPLE_REPORT_TOP_LIST_OVERALL_SCORE[
                                                    _index_tuple.OPTION_NAME],
                                                TUPLE_REPORT_TOP_LIST_SHIFT[
                                                    _index_tuple.OPTION_NAME],
                                                ]

DICT_REPORT_TOP_LIST_DATA: dict = dict.fromkeys(LIST_REPORT_TOP_LIST_COLUMN_NAMES)

EMPTY_LIST_ENTIRE_ROW: list = ['', None, None, None, None, None, None, None, None, None, None, None, None, None]

INDEX_PRIMARY_KEY = LIST_REPORT_TOP_LIST_COLUMN_NAMES.index(TUPLE_REPORT_TOP_LIST_QUOTE_ISIN[
                                                        _index_tuple.OPTION_NAME])
