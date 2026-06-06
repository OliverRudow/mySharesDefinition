"""myPerformanceWatchListDefinitions.py."""

__title__: str = "myPerformanceWatchListDefinitions"
__version__: str = "0.1.1"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from data_base_me.mySQLDataBase import STR_SQL_DATA_BASE_NAME, STR_SQL_DATA_DIR_NAME
from tuple_me import myTuple

def init_dict_performance_watch_list_data() -> dict[str, str | None]:
    elem = 0

    for key in DICT_PERFORMANCE_WATCH_LIST_DATA:

        DICT_PERFORMANCE_WATCH_LIST_DATA[key] = EMPTY_LIST_ENTIRE_ROW[elem]

        elem += 1

    return DICT_PERFORMANCE_WATCH_LIST_DATA

STR_DATA_BASE_FILE_NAME: str = STR_SQL_DATA_BASE_NAME

STR_DATA_BASE_DIR_NAME: str = STR_SQL_DATA_DIR_NAME

STR_DATA_BASE_TABLE_NAME: str = 'performance_watch_list'

STR_DATA_BASE_TABLE_EVAL_NAME: str = STR_DATA_BASE_TABLE_NAME + '_eval'

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 5.0

DATA_BASE_CONNECTION_URI: bool = True

DATA_BASE_FLAG_ADD_DATE: bool = True

DATA_BASE_FLAG_CLEAN_PRECEDED_DATA: bool = True

DATA_BASE_INT_NUMBER_PRECEDED_DATA = 20

LIST_SECTIONS_WATCH_LIST: list[str] = ['TUPLE_PERFORMANCE_WATCH_LIST_QUOTE_ISIN',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_ASK',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_ASK_SIZE',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_BID',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_BID_SIZE',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_CURRENT_PRICE',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_DAY_HIGH',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_DAY_LOW',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_DAILY_SPAN',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_INTERDAY_MOMENTUM',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_OPEN',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_PREVIOUS_CLOSE',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_INTRADAY_MOMENTUM',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_REGULAR_MARKET_CHANGE_PERCENT',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_VOLUME',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_VOLUME',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_DAILY_VOLUME_10_DAY',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME_10_DAY',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_BETA',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW_MOMENTUM',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH_MOMENTUM',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_AVERAGE',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_MOMENTUM',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_AVERAGE',
                                       'TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_MOMENTUM',]

TUPLE_PERFORMANCE_WATCH_LIST_QUOTE_ISIN: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.QUOTE_ISIN',
    'quote_isin',
    ('quote_isin', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_ASK: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.ASK',
    'ask',
    ('ask', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_ASK_SIZE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.ASK_SIZE',
    'ask_size',
    ('ask_size', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_BID: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.BID',
    'bid',
    ('bid', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_BID_SIZE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.BID_SIZE',
    'bid_size',
    ('bid_size', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_CURRENT_PRICE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.CURRENT_PRICE',
    'current_price',
    ('current_price', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_DAY_HIGH: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.DAY_HIGH',
    'day_high',
    ('day_high', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_DAY_LOW: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.DAY_LOW',
    'day_low',
    ('day_low', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_DAILY_SPAN: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.RELATIVE_DAILY_SPAN',
    'relative_daily_span',
    ('relative_daily_span', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_INTERDAY_MOMENTUM: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.INTERDAY_MOMENTUM',
    'interday_momentum',
    ('interday_momentum', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_OPEN: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.OPEN',
    'open',
    ('open', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_PREVIOUS_CLOSE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.PREVIOUS_CLOSE',
    'previous_close',
    ('previous_close', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_REGULAR_MARKET_CHANGE_PERCENT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.REGULAR_MARKET_CHANGE_PERCENT',
    'regular_market_change_percent',
    ('regular_market_change_percent', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_INTRADAY_MOMENTUM: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.INTRADAY_MOMENTUM',
    'intraday_momentum',
    ('intraday_momentum', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_VOLUME: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.VOLUME',
    'volume',
    ('volume', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_VOLUME: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.AVERAGE_VOLUME',
    'average_volume',
    ('average_volume', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.RELATIVE_VOLUME',
    'relative_volume',
    ('relative_volume', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_DAILY_VOLUME_10_DAY: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.AVERAGE_DAILY_VOLUME_10_DAY',
    'average_daily_volume_10_day',
    ('average_daily_volume_10_day', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME_10_DAY: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.RELATIVE_VOLUME_10_DAY',
    'relative_volume_10_day',
    ('relative_volume_10_day', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_BETA: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.BETA',
    'beta',
    ('beta', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.FIFTY_TWO_WEEK_LOW',
    'fifty_two_week_low',
    ('fifty_two_week_low', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW_MOMENTUM: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.FIFTY_TWO_WEEK_LOW_MOMENTUM',
    'fifty_two_week_low_momentum',
    ('fifty_two_week_low_momentum', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.FIFTY_TWO_WEEK_HIGH',
    'fifty_two_week_high',
    ('fifty_two_week_high', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH_MOMENTUM: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.FIFTY_TWO_WEEK_HIGH_MOMENTUM',
    'fifty_two_week_high_momentum',
    ('fifty_two_week_high_momentum', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_AVERAGE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.FIFTY_DAY_AVERAGE',
    'fifty_day_average',
    ('fifty_day_average', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_MOMENTUM: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.FIFTY_DAY_MOMENTUM',
    'fifty_day_momentum',
    ('fifty_day_momentum', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_AVERAGE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.TWO_HUNDRED_DAY_AVERAGE',
    'two_hundred_day_average',
    ('two_hundred_day_average', 'REAL'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_MOMENTUM: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST.TWO_HUNDRED_DAY_MOMENTUM',
    'two_hundred_day_momentum',
    ('two_hundred_day_momentum', 'REAL'),
    tuple)

_index_tuple = myTuple.MyTuple

LIST_PERFORMANCE_WATCH_LIST_COLUMN_NAMES: list[str] = [TUPLE_PERFORMANCE_WATCH_LIST_QUOTE_ISIN[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_ASK[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_ASK_SIZE[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_BID[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_BID_SIZE[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_CURRENT_PRICE[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_DAY_HIGH[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_DAY_LOW[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_DAILY_SPAN[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_INTERDAY_MOMENTUM[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_OPEN[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_PREVIOUS_CLOSE[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_INTRADAY_MOMENTUM[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_REGULAR_MARKET_CHANGE_PERCENT[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_INTRADAY_MOMENTUM[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_VOLUME[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_VOLUME[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_DAILY_VOLUME_10_DAY[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME_10_DAY[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_BETA[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW_MOMENTUM[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH_MOMENTUM[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_AVERAGE[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_MOMENTUM[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_AVERAGE[
                                                        _index_tuple.OPTION_NAME],
                                                      TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_MOMENTUM[
                                                        _index_tuple.OPTION_NAME]]

DICT_PERFORMANCE_WATCH_LIST_DATA: dict = dict.fromkeys(LIST_PERFORMANCE_WATCH_LIST_COLUMN_NAMES)

EMPTY_LIST_ENTIRE_ROW: list = ['', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                               None, None, None, None, None, None, None, None, None, None, None, None, None]

INDEX_PRIMARY_KEY = LIST_PERFORMANCE_WATCH_LIST_COLUMN_NAMES.index(TUPLE_PERFORMANCE_WATCH_LIST_QUOTE_ISIN[
                                                        _index_tuple.OPTION_NAME])

LIST_SECTIONS_WATCH_LIST_EVAL: list[str] = ['TUPLE_PERFORMANCE_WATCH_LIST_EVAL_QUOTE_ISIN',
                                            'TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_DAILY_SPAN',
                                            'TUPLE_PERFORMANCE_WATCH_LIST_EVAL_INTERDAY_MOMENTUM',
                                            'TUPLE_PERFORMANCE_WATCH_LIST_EVAL_INTRADAY_MOMENTUM',
                                            'TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_VOLUME',
                                            'TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_VOLUME_10_DAY',
                                            'TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_TWO_WEEKS_LOW_MOMENTUM',
                                            'TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_TWO_WEEKS_HIGH_MOMENTUM',
                                            'TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_DAY_MOMENTUM',
                                            'TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWO_HUNDRED_DAY_MOMENTUM',
                                            'TUPLE_PERFORMANCE_WATCH_LIST_EVAL_SECTION_CHANGE_PERCENT',
                                            'TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT_JSON_OBJECT',
                                            'TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT',
                                            'TUPLE_PERFORMANCE_WATCH_LIST_EVAL_ABSOLUTE_SCORE']

TUPLE_PERFORMANCE_WATCH_LIST_EVAL_QUOTE_ISIN: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST_EVAL.QUOTE_ISIN',
    'quote_isin',
    ('quote_isin', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_DAILY_SPAN: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST_EVAL.RELATIVE_DAILY_SPAN',
    'relative_daily_span_eval',
    ('relative_daily_span_eval', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_EVAL_INTERDAY_MOMENTUM: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST_EVAL.INTERDAY_MOMENTUM',
    'interday_momentum_eval',
    ('interday_momentum_eval', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_EVAL_INTRADAY_MOMENTUM: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST_EVAL.INTRADAY_MOMENTUM',
    'intraday_momentum_eval',
    ('intraday_momentum_eval', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_VOLUME: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST_EVAL.RELATIVE_VOLUME',
    'relative_volume_eval',
    ('relative_volume_eval', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_VOLUME_10_DAY: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST_EVAL.RELATIVE_VOLUME_10_DAY',
    'relative_volume_10_day_eval',
    ('relative_volume_10_day_eval', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_TWO_WEEKS_LOW_MOMENTUM: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST_EVAL.FIFTY_TWO_WEEKS_LOW_MOMENTUM',
    'fifty_two_weeks_low_eval',
    ('fifty_two_weeks_low_eval', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_TWO_WEEKS_HIGH_MOMENTUM: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST_EVAL.FIFTY_TWO_WEEKS_HIGH_MOMENTUM',
    'fifty_two_weeks_high_eval',
    ('fifty_two_weeks_high_eval', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_DAY_MOMENTUM: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST_EVAL.FIFTY_DAY_MOMENTUM',
    'fifty_day_average_eval',
    ('fifty_day_average_eval', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWO_HUNDRED_DAY_MOMENTUM: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST_EVAL.TWO_HUNDRED_DAY_MOMENTUM',
    'two_hundred_day_average_eval',
    ('two_hundred_day_average_eval', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_EVAL_SECTION_CHANGE_PERCENT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST_EVAL_SECTION_CHANGE_PERCENT',
    'section_change_percent',
    ('section_change_percent', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT_JSON_OBJECT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT_JSON_OBJECT',
    'twenty_day_change_percent_jsom_object',
    ('twenty_day_change_percent_jsom_object', 'BLOB'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT',
    'twenty_day_change_percent',
    ('twenty_day_change_percent', 'INTEGER'),
    tuple)

TUPLE_PERFORMANCE_WATCH_LIST_EVAL_ABSOLUTE_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('PERFORMANCE_WATCH_LIST_EVAL.ABSOLUTE_SCORE',
    'absolute_score_eval',
    ('absolute_score_eval', 'REAL'),
    tuple)

LIST_PERFORMANCE_WATCH_LIST_EVAL_COLUMN_NAMES: list[str] = [TUPLE_PERFORMANCE_WATCH_LIST_EVAL_QUOTE_ISIN[
                                                        _index_tuple.OPTION_NAME],
                                                        TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_DAILY_SPAN[
                                                        _index_tuple.OPTION_NAME],
                                                        TUPLE_PERFORMANCE_WATCH_LIST_EVAL_INTERDAY_MOMENTUM[
                                                        _index_tuple.OPTION_NAME],
                                                        TUPLE_PERFORMANCE_WATCH_LIST_EVAL_INTRADAY_MOMENTUM[
                                                        _index_tuple.OPTION_NAME],
                                                        TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_VOLUME[
                                                        _index_tuple.OPTION_NAME],
                                                        TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_VOLUME_10_DAY[
                                                        _index_tuple.OPTION_NAME],
                                                        TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_TWO_WEEKS_LOW_MOMENTUM[
                                                        _index_tuple.OPTION_NAME],
                                                        TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_TWO_WEEKS_HIGH_MOMENTUM[
                                                        _index_tuple.OPTION_NAME],
                                                        TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_DAY_MOMENTUM[
                                                        _index_tuple.OPTION_NAME],
                                                        TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWO_HUNDRED_DAY_MOMENTUM[
                                                        _index_tuple.OPTION_NAME],
                                                        TUPLE_PERFORMANCE_WATCH_LIST_EVAL_SECTION_CHANGE_PERCENT[
                                                        _index_tuple.OPTION_NAME],
                                                        TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT_JSON_OBJECT[
                                                        _index_tuple.OPTION_NAME],
                                                        TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT[
                                                        _index_tuple.OPTION_NAME],
                                                        TUPLE_PERFORMANCE_WATCH_LIST_EVAL_ABSOLUTE_SCORE[
                                                       _index_tuple.OPTION_NAME]]

STR_SCORE_TABLE_NAME: str = 'score_config'

TUPLE_SCORE_TABLE_MIN_THRESHOLD: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('SCORE_TABLE.MIN_THRESHOLD',
    'min_threshold',
    ('min_threshold', 'DECIMAL'),
    tuple)

TUPLE_SCORE_TABLE_CREDIT_POINTS: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('SCORE_TABLE.CREDIT_POINTS',
    'credit_points',
    ('credit_points', 'INTEGER'),
    tuple)

LIST_RELATIVE_DAILY_SPAN_SCORE_TABLE: list[tuple[float, int]] = [
    (0, 5),
    (0.5, 4),
    (1, 3),
    (2, 2),
    (3, 1),
    (4, 0),
    (5, -1),
    (10, -2),
    (20, -3),
    (30, -4),
    (100, -5)
]

LIST_INTERDAY_MOMENTUM_SCORE_TABLE: list[tuple[float, int]] = [
    (-100, 5),
    (0, 4),
    (0.25, 3),
    (0.5, 2),
    (0.75, 1),
    (1, 0),
    (2, -1),
    (3, -2),
    (5, -3),
    (10, -4),
    (100, -5)
]

LIST_INTRADAY_MOMENTUM_SCORE_TABLE: list[tuple[float, int]] = [
    (10, 5),
    (5, 4),
    (2.5, 3),
    (1, 2),
    (0, 1),
    (-0.1, 0),
    (-0.5, -1),
    (-1, -2),
    (-2.5, -3),
    (-5, -4),
    (-100, -5)
]

LIST_RELATIVE_VOLUME_SCORE_TABLE: list[tuple[float, int]] = [
    (20, 5),
    (10, 4),
    (5, 3),
    (2.5, 2),
    (1, 1),
    (0.5, 0),
    (0.1, -1),
    (0.05, -2),
    (0.01, -3),
    (0.005, -4),
    (0, -5)
]

LIST_RELATIVE_VOLUME_10_DAY_SCORE_TABLE: list[tuple[float, int]] = [
    (100, 5),
    (10, 4),
    (5, 3),
    (2.5, 2),
    (1, 1),
    (0.75, 0),
    (0.5, -1),
    (0.25, -2),
    (0.1, -3),
    (0.01, -4),
    (0, -5)
]

LIST_FIFTY_TWO_WEEKS_LOW_MOMENTUM_TABLE: list[tuple[float, int]] = [
    (1000, 5),
    (500, 4),
    (200, 3),
    (100, 2),
    (50, 1),
    (20, 0),
    (10, -1),
    (5, -2),
    (2, -3),
    (1, -4),
    (0, -5)
]

LIST_FIFTY_TWO_WEEKS_HIGH_MOMENTUM_TABLE: list[tuple[float, int]] = [
    (-1, 5),
    (-2.5, 4),
    (-5, 3),
    (-7.5, 2),
    (-10, 1),
    (-12.5, 0),
    (-15, -1),
    (-17.5, -2),
    (-20, -3),
    (-50, -4),
    (-1000, -5)
]

LIST_FIFTY_DAY_MOMENTUM_TABLE: list[tuple[float, int]] = [
    (100, 5),
    (75, 4),
    (50, 3),
    (25, 2),
    (10, 1),
    (5, 0),
    (1, -1),
    (-1, -2),
    (-5, -3),
    (-10, -4),
    (-1000, -5)
]

LIST_TWO_HUNDRED_DAY_MOMENTUM_TABLE: list[tuple[float, int]] = [
    (100, 5),
    (75, 4),
    (50, 3),
    (25, 2),
    (10, 1),
    (5, 0),
    (1, -1),
    (-1, -2),
    (-5, -3),
    (-10, -4),
    (-1000, -5)
]

LIST_TWENTY_DAY_CHANGE_PERCENT_RATIO: list[tuple[float, int]] = [
    (0.95, 4),
    (0.65, 5),
    (0.6, 4),
    (0.55, 3),
    (0.5, 2),
    (0.45, 0),
    (0.4, -2),
    (0.3, -3),
    (0.2, -4),
    (0, -5),
]

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
    ('weight_1', 0.5),
    ('weight_2', 0.5),
    ('weight_3', 0.5),
    ('weight_4', 0.5),
    ('weight_5', 0.5),
    ('weight_6', 0.5),
    ('weight_7', 0.5),
    ('weight_8', 0.5),
    ('weight_9', 0.5),
    ('weight_10', 0.5),
    ('weight_11', 0.5),
]

