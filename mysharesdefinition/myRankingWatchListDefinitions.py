"""myRankingWatchListDefinitions.py."""

__title__: str = "myRankingWatchListDefinitions"
__version__: str = "0.3.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from mydatabase.mySQLDataBase import STR_SQL_DATA_BASE_NAME, STR_SQL_DATA_DIR_NAME
from mysharesdefinition import myPerformanceWatchListDefinitions, myFundamentalsWatchListDefinitions, \
    myAnalystWatchListDefinitions, myDerivateWatchListDefinitions
from mytuple import myTuple


STR_DATA_BASE_FILE_NAME: str = STR_SQL_DATA_BASE_NAME

STR_DATA_BASE_DIR_NAME: str = STR_SQL_DATA_DIR_NAME

STR_DATA_BASE_TABLE_NAME: str = 'ranking_watch_list'

STR_DATA_BASE_TABLE_NAME_COPY: str = STR_DATA_BASE_TABLE_NAME + '_old'

STR_DATA_BASE_TABLE_NAME_ANALYST: str = myAnalystWatchListDefinitions.STR_DATA_BASE_TABLE_EVAL_NAME

STR_DATA_BASE_TABLE_NAME_DERIVATE: str = myDerivateWatchListDefinitions.STR_DATA_BASE_TABLE_EVAL_NAME

STR_DATA_BASE_TABLE_NAME_FUNDAMENTALS: str = myFundamentalsWatchListDefinitions.STR_DATA_BASE_TABLE_EVAL_NAME

STR_DATA_BASE_TABLE_NAME_PERFORMANCE: str = myPerformanceWatchListDefinitions.STR_DATA_BASE_TABLE_EVAL_NAME

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 10.0

DATA_BASE_CONNECTION_URI: bool = True

LIST_SECTIONS_WATCH_LIST: list[str] = ['TUPLE_RANKING_WATCH_LIST_QUOTE_ISIN',
                                       'TUPLE_RANKING_WATCH_LIST_ANALYST_SCORE',
                                       'TUPLE_RANKING_WATCH_LIST_DERIVATE_SCORE',
                                       'TUPLE_RANKING_WATCH_LIST_FUNDAMENTALS_SCORE',
                                       'TUPLE_RANKING_WATCH_LIST_PERFORMANCE_SCORE',
                                       'TUPLE_RANKING_WATCH_LIST_OVERALL_SCORE',
                                       'TUPLE_RANKING_WATCH_LIST_SHIFT']

TUPLE_RANKING_WATCH_LIST_QUOTE_ISIN: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('RANKING_WATCH_LIST.QUOTE_ISIN',
     'quote_isin',
    ('quote_isin', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_RANKING_WATCH_LIST_ANALYST_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('RANKING_WATCH_LIST.ANALYST_SCORE',
     'analyst_score',
    ('analyst_score', 'REAL'),
    tuple)

TUPLE_RANKING_WATCH_LIST_DERIVATE_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('RANKING_WATCH_LIST.DERIVATE_SCORE',
     'derivate_score',
    ('derivate_score', 'REAL'),
    tuple)

TUPLE_RANKING_WATCH_LIST_FUNDAMENTALS_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('RANKING_WATCH_LIST.FUNDAMENTALS_SCORE',
     'fundamentals_score',
    ('fundamentals_score', 'REAL'),
    tuple)

TUPLE_RANKING_WATCH_LIST_PERFORMANCE_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('RANKING_WATCH_LIST.PERFORMANCE_SCORE',
     'performance_score',
    ('performance_score', 'REAL'),
    tuple)

TUPLE_RANKING_WATCH_LIST_OVERALL_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('RANKING_WATCH_LIST.OVERALL_SCORE',
     'overall_score',
    ('overall_score', 'REAL'),
    tuple)

TUPLE_RANKING_WATCH_LIST_SHIFT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('RANKING_WATCH_LIST.SHIFT',
     'shift',
    ('shift', 'INTEGER'),
    tuple)

_index_tuple = myTuple.MyTuple

LIST_STATIC_WATCH_LIST_COLUMN_NAMES: list[str] = [TUPLE_RANKING_WATCH_LIST_QUOTE_ISIN[
                                                      _index_tuple.OPTION_NAME],
                                                  TUPLE_RANKING_WATCH_LIST_ANALYST_SCORE[
                                                      _index_tuple.OPTION_NAME],
                                                  TUPLE_RANKING_WATCH_LIST_DERIVATE_SCORE[
                                                      _index_tuple.OPTION_NAME],
                                                  TUPLE_RANKING_WATCH_LIST_FUNDAMENTALS_SCORE[
                                                      _index_tuple.OPTION_NAME],
                                                  TUPLE_RANKING_WATCH_LIST_PERFORMANCE_SCORE[
                                                      _index_tuple.OPTION_NAME],
                                                  TUPLE_RANKING_WATCH_LIST_OVERALL_SCORE[
                                                      _index_tuple.OPTION_NAME],
                                                  TUPLE_RANKING_WATCH_LIST_SHIFT[
                                                      _index_tuple.OPTION_NAME]]

STR_SCORE_TABLE_NAME: str = 'score_config'

TUPLE_SCORE_TABLE_WEIGHT_NAME: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('SCORE_TABLE.WEIGHT_NAME',
    'weight_name',
    ('weight_name', 'TEXT'),
    tuple)

TUPLE_SCORE_TABLE_WEIGHT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('SCORE_TABLE.WEIGHT',
    'weight',
    ('weight', 'REAL'),
    tuple)

LIST_WEIGHT_SCORE_TABLE: list[tuple[str, float]] = [
    ('weight_1', 0.25),
    ('weight_2', 0.25),
    ('weight_3', 0.5),
    ('weight_4', 0.5),
    ]
