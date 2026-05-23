"""myAnalystWatchListDefinitions.py."""

__title__: str = "myAnalystWatchListDefinitions"
__version__: str = "0.1.1"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from data_base_me.mySQLDataBase import STR_SQL_DATA_BASE_NAME, STR_SQL_DATA_DIR_NAME
from tuple_me import myTuple

def init_dict_analyst_watch_list_data() -> dict[str, str | bool | None]:
    elem = 0

    for key in DICT_ANALYST_WATCH_LIST_DATA:

        DICT_ANALYST_WATCH_LIST_DATA[key] = EMPTY_LIST_ENTIRE_ROW[elem]

        elem += 1

    return DICT_ANALYST_WATCH_LIST_DATA

STR_DATA_BASE_FILE_NAME: str = STR_SQL_DATA_BASE_NAME

STR_DATA_BASE_DIR_NAME: str = STR_SQL_DATA_DIR_NAME

STR_DATA_BASE_TABLE_NAME: str = 'analyst_watch_list'

STR_DATA_BASE_TABLE_EVAL_NAME: str = 'analyst_watch_list_eval'

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 5.0

DATA_BASE_CONNECTION_URI: bool = True

DATA_BASE_FLAG_ADD_DATE: bool = False

DATA_BASE_FLAG_CLEAN_PRECEDED_DATA: bool = False

DATA_BASE_INT_NUMBER_PRECEDED_DATA = 0

LIST_SECTIONS_WATCH_LIST: list[str] = ['TUPLE_ANALYST_WATCH_LIST_QUOTE_ISIN',
                                       'TUPLE_ANALYST_WATCH_LIST_CURRENT_PRICE',
                                       'TUPLE_ANALYST_WATCH_LIST_TARGET_HIGH_PRICE',
                                       'TUPLE_ANALYST_WATCH_LIST_TARGET_LOW_PRICE',
                                       'TUPLE_ANALYST_WATCH_LIST_TARGET_MEAN_PRICE',
                                       'TUPLE_ANALYST_WATCH_LIST_TARGET_MEDIAN_PRICE',
                                       'TUPLE_ANALYST_WATCH_LIST_UPSIDE_POTENTIAL',
                                       'TUPLE_ANALYST_WATCH_LIST_RISK_REWARD_RATIO',
                                       'TUPLE_ANALYST_WATCH_LIST_ANALYST_DISPERSION',
                                       'TUPLE_ANALYST_WATCH_LIST_RECOMMENDATION_MEAN',
                                       'TUPLE_ANALYST_WATCH_LIST_RECOMMENDATION_KEY',
                                       'TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_INDEX',
                                       'TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_TREND',
                                       'TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_TREND_CREDIT',
                                       'TUPLE_ANALYST_WATCH_LIST_NUMBER_OF_ANALYST_OPINIONS']

TUPLE_ANALYST_WATCH_LIST_QUOTE_ISIN: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.QUOTE_ISIN',
    'quote_isin',
    ('quote_isin', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_CURRENT_PRICE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.CURRENT_PRICE',
    'current_price',
    ('current_price', 'REAL'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_TARGET_HIGH_PRICE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.TARGET_HIGH_PRICE',
    'target_high_price',
    ('target_high_price', 'REAL'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_TARGET_LOW_PRICE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.TARGET_LOW_PRICE',
    'target_low_price',
    ('target_low_price', 'REAL'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_TARGET_MEAN_PRICE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.TARGET_MEAN_PRICE',
    'target_mean_price',
    ('target_mean_price', 'REAL'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_TARGET_MEDIAN_PRICE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.TARGET_MEDIAN_PRICE',
    'target_median_price',
    ('target_median_price', 'REAL'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_UPSIDE_POTENTIAL: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.UPSIDE_POTENTIAL',
    'upside_potential',
    ('upside_potential', 'REAL'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_RISK_REWARD_RATIO: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.RISK_REWARD_RATIO',
    'risk_reward_ratio',
    ('risk_reward_ratio', 'REAL'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_ANALYST_DISPERSION: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.RISK_REWARD_RATIO',
    'analyst_dispersion',
    ('analyst_dispersion', 'REAL'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_RECOMMENDATION_MEAN: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.RECOMMENDATION_MEAN',
    'recommendation_mean',
    ('recommendation_mean', 'REAL'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_RECOMMENDATION_KEY: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.RECOMMENDATION_KEY',
    'recommendation_key',
    ('recommendation_key', 'TEXT'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_INDEX: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.WEIGHTED_REVISION_INDEX',
    'weighted_revision_index',
    ('weighted_revision_index', 'REAL'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_TREND: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.WEIGHTED_REVISION_INDEX',
    'weighted_revision_trend',
    ('weighted_revision_trend', 'TEXT'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_TREND_CREDIT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.WEIGHTED_REVISION_INDEX_CREDIT',
    'weighted_revision_trend_credit',
    ('weighted_revision_trend_credit', 'REAL'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_NUMBER_OF_ANALYST_OPINIONS: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.NUMBER_OF_ANALYST_OPINIONS',
    'number_of_analyst_opinions',
    ('number_of_analyst_opinions', 'INTEGER'),
    tuple)


_index_tuple = myTuple.MyTuple

LIST_ANALYST_WATCH_LIST_COLUMN_NAMES: list[str] = [TUPLE_ANALYST_WATCH_LIST_QUOTE_ISIN[
                                                        _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_CURRENT_PRICE[
                                                        _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_TARGET_HIGH_PRICE[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_TARGET_LOW_PRICE[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_TARGET_MEAN_PRICE[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_TARGET_MEDIAN_PRICE[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_UPSIDE_POTENTIAL[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_RISK_REWARD_RATIO[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_ANALYST_DISPERSION[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_RECOMMENDATION_MEAN[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_RECOMMENDATION_KEY[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_INDEX[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_TREND[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_TREND_CREDIT[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_NUMBER_OF_ANALYST_OPINIONS[
                                                       _index_tuple.OPTION_NAME]]

DICT_ANALYST_WATCH_LIST_DATA: dict = dict.fromkeys(LIST_ANALYST_WATCH_LIST_COLUMN_NAMES)

EMPTY_LIST_ENTIRE_ROW: list = ['', None, None, None, None, None, None, None, None, None, None, None, None, None, None]

INDEX_PRIMARY_KEY = LIST_ANALYST_WATCH_LIST_COLUMN_NAMES.index(TUPLE_ANALYST_WATCH_LIST_QUOTE_ISIN[
                                                        _index_tuple.OPTION_NAME])

LIST_SECTIONS_WATCH_LIST_EVAL: list[str] = ['TUPLE_ANALYST_WATCH_LIST_EVAL_QUOTE_ISIN',
                                       'TUPLE_ANALYST_WATCH_LIST_EVAL_UPSIDE_POTENTIAL',
                                       'TUPLE_ANALYST_WATCH_LIST_EVAL_RISK_REWARD_RATIO',
                                       'TUPLE_ANALYST_WATCH_LIST_EVAL_ANALYST_DISPERSION',
                                       'TUPLE_ANALYST_WATCH_LIST_EVAL_RECOMMENDATION_MEAN',
                                       'TUPLE_ANALYST_WATCH_LIST_EVAL_WEIGHTED_REVISION_INDEX',
                                       'TUPLE_ANALYST_WATCH_LIST_EVAL_WEIGHTED_REVISION_TREND_CREDIT',
                                       'TUPLE_ANALYST_WATCH_LIST_EVAL_NUMBER_OF_ANALYST_OPINIONS',
                                       'TUPLE_ANALYST_WATCH_LIST_EVAL_ABSOLUTE_SCORE']

TUPLE_ANALYST_WATCH_LIST_EVAL_QUOTE_ISIN: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST_EVAL.QUOTE_ISIN',
    'quote_isin',
    ('quote_isin', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_EVAL_UPSIDE_POTENTIAL: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST_EVAL.UPSIDE_POTENTIAL',
    'upside_potential_eval',
    ('upside_potential_eval', 'INTEGER'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_EVAL_RISK_REWARD_RATIO: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST.RISK_REWARD_RATIO',
    'risk_reward_ratio_eval',
    ('risk_reward_ratio_eval', 'INTEGER'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_EVAL_ANALYST_DISPERSION: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST_EVAL.ANALYST_DISPERSION',
    'analyst_dispersion_eval',
    ('analyst_dispersion_eval', 'INTEGER'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_EVAL_RECOMMENDATION_MEAN: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST_EVAL.RECOMMENDATION_MEAN',
    'recommendation_mean_eval',
    ('recommendation_mean_eval', 'INTEGER'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_EVAL_WEIGHTED_REVISION_INDEX: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST_EVAL.WEIGHTED_REVISION_INDEX',
    'weighted_revision_index_eval',
    ('weighted_revision_index_eval', 'INTEGER'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_EVAL_WEIGHTED_REVISION_TREND_CREDIT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST_EVAL.WEIGHTED_REVISION_INDEX_CREDIT',
    'weighted_revision_trend_eval',
    ('weighted_revision_trend_eval', 'REAL'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_EVAL_NUMBER_OF_ANALYST_OPINIONS: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST_EVAL.NUMBER_OF_ANALYST_OPINIONS',
    'number_of_analyst_opinions_eval',
    ('number_of_analyst_opinions_eval', 'INTEGER'),
    tuple)

TUPLE_ANALYST_WATCH_LIST_EVAL_ABSOLUTE_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ANALYST_WATCH_LIST_EVAL.ABSOLUTE_SCORE',
    'absolute_score_eval',
    ('absolute_score_eval', 'REAL'),
    tuple)

LIST_ANALYST_WATCH_LIST_EVAL_COLUMN_NAMES: list[str] = [TUPLE_ANALYST_WATCH_LIST_EVAL_QUOTE_ISIN[
                                                        _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_EVAL_UPSIDE_POTENTIAL[
                                                        _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_EVAL_RISK_REWARD_RATIO[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_EVAL_ANALYST_DISPERSION[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_EVAL_RECOMMENDATION_MEAN[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_EVAL_WEIGHTED_REVISION_INDEX[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_EVAL_WEIGHTED_REVISION_TREND_CREDIT[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_EVAL_NUMBER_OF_ANALYST_OPINIONS[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_ANALYST_WATCH_LIST_EVAL_ABSOLUTE_SCORE[
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

LIST_UPSIDE_POTENTIAL_SCORE_TABLE: list[tuple[float, int]] = [
    (0.2, 5),
    (0.15, 4),
    (0.1, 3),
    (0.05, 2),
    (0, 1),
    (-0.05, -1),
    (-0.1, -2),
    (-0.15, -3),
    (-0.2, -4),
    (-1, -5)
]

LIST_RISK_REWARD_SCORE_TABLE: list[tuple[float, int]] = [
    (5, -5),
    (4, -4),
    (3, -3),
    (2,  -2),
    (1,  -1),
    (0.5,  -1),
    (0.33, -2),
    (0.25, -3),
    (0.2, -4),
    (0.01, -5)
]

LIST_ANALYST_DISPERSION_SCORE_TABLE: list[tuple[float, int]] = [
    (1.25, -3),
    (1.00, -2),
    (0.75, -1),
    (0.50,  1),
    (0.25,  2),
    (0.00,  3)
]

LIST_RECOMMENDATION_MEAN_SCORE_TABLE: list[tuple[float, int]] = [
    (5, 1),
    (4, 2),
    (3, 3),
    (2,  4),
    (1,  5)
]

LIST_WEIGHTED_REVISION_SCORE_TABLE: list[tuple[float, int]] = [
    (0.8,5),
    (0.6,4),
    (0.4,3),
    (0.2,2),
    (0,  1),
    (-0.2,0),
    (-0.4,-1),
    (-0.6, -2),
    (-0.8, -3),
    (-10, -4) 
]

LIST_NUMBER_ANALYST_OPINIONS_SCORE_TABLE: list[tuple[float, int]] = [
    (40.0,2),
    (30.0,1),
    (20.0,0),
    (10.0,-1),
    (0, -2)
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
]