"""myDerivateWatchListDefinitions.py."""

__title__: str = "myDerivateWatchListDefinitions"
__version__: str = "0.3.0"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from mydatabase.mySQLDataBase import STR_SQL_DATA_BASE_NAME, STR_SQL_DATA_DIR_NAME
from mytuple import myTuple

def init_dict_derivate_watch_list_data() -> dict[str, str | int |  float | None]:
    elem = 0

    for key in DICT_DERIVATE_WATCH_LIST_DATA:

        DICT_DERIVATE_WATCH_LIST_DATA[key] = EMPTY_LIST_ENTIRE_ROW[elem]

        elem += 1

    return DICT_DERIVATE_WATCH_LIST_DATA

STR_DATA_BASE_FILE_NAME: str = STR_SQL_DATA_BASE_NAME

STR_DATA_BASE_DIR_NAME: str = STR_SQL_DATA_DIR_NAME

STR_DATA_BASE_TABLE_NAME: str = 'derivate_watch_list'

STR_DATA_BASE_TABLE_EVAL_NAME: str = 'derivate_watch_list_eval'

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 5.0

DATA_BASE_CONNECTION_URI: bool = True

DATA_BASE_FLAG_ADD_DATE: bool = False

DATA_BASE_FLAG_CLEAN_PRECEDED_DATA: bool = False

DATA_BASE_INT_NUMBER_PRECEDED_DATA = 0

LIST_SECTIONS_WATCH_LIST: list[str] = ['TUPLE_DERIVATE_WATCH_LIST_QUOTE_ISIN',
                                       'TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT',
                                       'TUPLE_DERIVATE_WATCH_LIST_FLOAT_SHARES',
                                       'TUPLE_DERIVATE_WATCH_LIST_SHORT_PERCENT_OF_FLOAT',
                                       'TUPLE_DERIVATE_WATCH_LIST_SHARES_OUTSTANDING',
                                       'TUPLE_DERIVATE_WATCH_LIST_SHORT_RATIO',
                                       'TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT_PRIOR_MONTH',
                                       'TUPLE_DERIVATE_WATCH_LIST_SHORT_PERCENT_CHANGE',
                                       'TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT_PREVIOUS_MONTH_DATE',
                                       'TUPLE_DERIVATE_WATCH_LIST_SHORT_DATE_DELTA_LAST_MONTH',
                                       'TUPLE_DERIVATE_WATCH_LIST_SHORT_DATE_DELTA_THIS_MONTH',
                                       'TUPLE_DERIVATE_WATCH_LIST_DATE_SHORT_INTEREST',
                                       'TUPLE_DERIVATE_WATCH_LIST_HELD_PERCENT_INSIDERS',
                                       'TUPLE_DERIVATE_WATCH_LIST_HELD_PERCENT_INSTITUTIONS']

TUPLE_DERIVATE_WATCH_LIST_QUOTE_ISIN: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST.QUOTE_ISIN',
    'quote_isin',
    ('quote_isin', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST.SHARES_SHORT',
    'shares_short',
    ('shares_short', 'INTEGER'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_FLOAT_SHARES: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST.FLOAT_SHARES',
    'float_shares',
    ('float_shares', 'INTEGER'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_SHORT_PERCENT_OF_FLOAT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST.SHORT_PERCENT_OF_FLOAT',
    'short_percent_of_float',
    ('short_percent_of_float', 'REAL'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_SHARES_OUTSTANDING: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST.SHARES_OUTSTANDING',
    'shares_outstanding',
    ('shares_outstanding', 'INTEGER'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_SHORT_RATIO: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST.SHORT_RATIO',
    'short_ratio',
    ('short_ratio', 'REAL'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT_PRIOR_MONTH: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST.SHARES_SHORT_PRIOR_MONTH',
    'shares_short_prior_month',
    ('shares_short_prior_month', 'INTEGER'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_SHORT_PERCENT_CHANGE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST.SHORT_PERCENT_CHANGE',
    'short_percent_change',
    ('short_percent_change', 'REAL'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT_PREVIOUS_MONTH_DATE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST.SHARES_SHORT_PREVIOUS_MONTH_DATE',
    'shares_short_previous_month_date',
    ('shares_short_previous_month_date', 'INTEGER'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_DATE_SHORT_INTEREST: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST.DATE_SHORT_INTEREST',
    'date_short_interest',
    ('date_short_interest', 'INTEGER'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_SHORT_DATE_DELTA_LAST_MONTH: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST.SHORT_DATE_DELTA_LAST_MONTH',
    'short_date_delta_last_month',
    ('short_date_delta_last_month', 'INTEGER'),
    tuple)


TUPLE_DERIVATE_WATCH_LIST_SHORT_DATE_DELTA_THIS_MONTH: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST.SHORT_DATE_DELTA_THIS_MONTH',
    'short_date_delta_this_month',
    ('short_date_delta_this_month', 'INTEGER'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_HELD_PERCENT_INSIDERS: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST.HELD_PERCENT_INSIDERS',
    'held_percent_insiders',
    ('held_percent_insiders', 'REAL'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_HELD_PERCENT_INSTITUTIONS: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST.HELD_PERCENT_INSTITUTIONS',
    'held_percent_institutions',
    ('held_percent_institutions', 'REAL'),
    tuple)

_index_tuple = myTuple.MyTuple

LIST_DERIVATE_WATCH_LIST_COLUMN_NAMES: list[str] = [TUPLE_DERIVATE_WATCH_LIST_QUOTE_ISIN[
                                                        _index_tuple.OPTION_NAME],
                                                    TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT[
                                                        _index_tuple.OPTION_NAME],
                                                    TUPLE_DERIVATE_WATCH_LIST_FLOAT_SHARES[
                                                        _index_tuple.OPTION_NAME],
                                                    TUPLE_DERIVATE_WATCH_LIST_SHORT_PERCENT_OF_FLOAT[
                                                        _index_tuple.OPTION_NAME],
                                                    TUPLE_DERIVATE_WATCH_LIST_SHARES_OUTSTANDING[
                                                        _index_tuple.OPTION_NAME],
                                                    TUPLE_DERIVATE_WATCH_LIST_SHORT_RATIO[
                                                        _index_tuple.OPTION_NAME],
                                                    TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT_PRIOR_MONTH[
                                                        _index_tuple.OPTION_NAME],
                                                    TUPLE_DERIVATE_WATCH_LIST_SHORT_PERCENT_CHANGE[
                                                        _index_tuple.OPTION_NAME],
                                                    TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT_PREVIOUS_MONTH_DATE[
                                                        _index_tuple.OPTION_NAME],
                                                    TUPLE_DERIVATE_WATCH_LIST_DATE_SHORT_INTEREST[
                                                        _index_tuple.OPTION_NAME],
                                                    TUPLE_DERIVATE_WATCH_LIST_SHORT_DATE_DELTA_LAST_MONTH[
                                                        _index_tuple.OPTION_NAME],
                                                    TUPLE_DERIVATE_WATCH_LIST_SHORT_DATE_DELTA_THIS_MONTH[
                                                        _index_tuple.OPTION_NAME],
                                                    TUPLE_DERIVATE_WATCH_LIST_HELD_PERCENT_INSIDERS[
                                                        _index_tuple.OPTION_NAME],
                                                    TUPLE_DERIVATE_WATCH_LIST_HELD_PERCENT_INSTITUTIONS[
                                                        _index_tuple.OPTION_NAME],
                                                   ]

DICT_DERIVATE_WATCH_LIST_DATA: dict = dict.fromkeys(LIST_DERIVATE_WATCH_LIST_COLUMN_NAMES)

EMPTY_LIST_ENTIRE_ROW: list = ['', None, None, None, None, None, None, None, None, None, None, None, None, None]

INDEX_PRIMARY_KEY = LIST_DERIVATE_WATCH_LIST_COLUMN_NAMES.index(TUPLE_DERIVATE_WATCH_LIST_QUOTE_ISIN[
                                                        _index_tuple.OPTION_NAME])

LIST_SECTIONS_WATCH_LIST_EVAL: list[str] = ['TUPLE_DERIVATE_WATCH_LIST_EVAL_QUOTE_ISIN',
                                            'TUPLE_DERIVATE_WATCH_LIST_EVAL_SHORT_PERCENT_OF_FLOAT',
                                            'TUPLE_DERIVATE_WATCH_LIST_EVAL_SHORT_RATIO',
                                            'TUPLE_DERIVATE_WATCH_LIST_EVAL_SHORT_PERCENT_CHANGE',
                                            'TUPLE_DERIVATE_WATCH_LIST_EVAL_SHORT_DATE_DELTA_THIS_MONTH',
                                            'TUPLE_DERIVATE_WATCH_LIST_EVAL_ABSOLUTE_SCORE']

TUPLE_DERIVATE_WATCH_LIST_EVAL_QUOTE_ISIN: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST_EVAL.QUOTE_ISIN',
    'quote_isin',
    ('quote_isin', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_EVAL_SHORT_PERCENT_OF_FLOAT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST_EVAL.SHORT_PERCENT_OF_FLOAT',
    'short_percent_of_float_credit',
    ('short_percent_of_float_credit', 'INTEGER'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_EVAL_SHORT_RATIO: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST_EVAL.SHORT_RATIO',
    'short_ratio_credit',
    ('short_ratio_credit', 'INTEGER'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_EVAL_SHORT_PERCENT_CHANGE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST_EVAL.SHORT_PERCENTAGE_CHANGE',
    'short_percent_change_credit',
    ('short_percent_change_credit', 'INTEGER'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_EVAL_SHORT_DATE_DELTA_THIS_MONTH: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST_EVAL.SHORT_DATE_DELTA_THIS_MONTH_CHANGE',
    'short_date_delta_this_month_credit',
    ('short_date_delta_this_month_credit', 'INTEGER'),
    tuple)

TUPLE_DERIVATE_WATCH_LIST_EVAL_ABSOLUTE_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('DERIVATE_WATCH_LIST_EVAL.ABSOLUTE_SCORE',
    'absolute_score_eval',
    ('absolute_score_eval', 'REAL'),
    tuple)

LIST_DERIVATE_WATCH_LIST_EVAL_COLUMN_NAMES: list[str] = [TUPLE_DERIVATE_WATCH_LIST_EVAL_QUOTE_ISIN[
                                                        _index_tuple.OPTION_NAME],
                                                   TUPLE_DERIVATE_WATCH_LIST_EVAL_SHORT_PERCENT_OF_FLOAT[
                                                        _index_tuple.OPTION_NAME],
                                                   TUPLE_DERIVATE_WATCH_LIST_EVAL_SHORT_RATIO[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_DERIVATE_WATCH_LIST_EVAL_SHORT_PERCENT_CHANGE[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_DERIVATE_WATCH_LIST_EVAL_SHORT_DATE_DELTA_THIS_MONTH[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_DERIVATE_WATCH_LIST_EVAL_ABSOLUTE_SCORE[
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

LIST_SHORT_PERCENT_OF_FLOAT_CREDIT_TABLE: list[tuple[float, int]] = [
    (0.0, 5),
    (0.005, 4),
    (0.01, 3),
    (0.05, 2),
    (0.1, 1),
    (0.5, 0),
    (1, -1),
    (5, -2),
    (10, -3),
    (20, -4),
    (100, -5)
]

LIST_SHORT_RATIO_CREDIT_TABLE: list[tuple[float, int]] = [
    (0.0, 5),
    (0.05, 4),
    (0.1, 3),
    (0.5, 2),
    (1, 1),
    (3, 0),
    (5, -1),
    (10, -2),
    (20, -3),
    (50, -4),
    (100, -5)
]

LIST_SHORT_CHANGE_CREDIT_TABLE: list[tuple[float, int]] = [
    (-100.0, 5),
    (-75.0, 4),
    (-50.0, 3),
    (-25.0, 2),
    (0, 1),
    (10.0, 0),
    (20.0, -1),
    (30.0, -2),
    (50.0, -3),
    (75.0, -4),
    (100, -5)
]

LIST_SHORT_DATE_DELTA_THIS_MONTH_CREDIT_TABLE: list[tuple[float, int]] = [
    (0, 5),
    (5, 4),
    (10, 3),
    (15, 2),
    (20, 1),
    (25, 0),
    (30, -1),
    (35, -2),
    (40, -3),
    (45, -4),
    (100, -5)
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
]
