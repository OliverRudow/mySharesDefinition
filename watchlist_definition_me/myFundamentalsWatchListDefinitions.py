"""myFundamentalsWatchListDefinitions.py."""

__title__: str = "myFundamentalsWatchListDefinitions"
__version__: str = "0.1.1"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from data_base_me.mySQLDataBase import STR_SQL_DATA_BASE_NAME, STR_SQL_DATA_DIR_NAME
from tuple_me import myTuple

def init_dict_fundamentals_watch_list_data() -> dict[str, str | bool | None]:
    elem = 0

    for key in DICT_FUNDAMENTALS_WATCH_LIST_DATA:

        DICT_FUNDAMENTALS_WATCH_LIST_DATA[key] = EMPTY_LIST_ENTIRE_ROW[elem]

        elem += 1

    return DICT_FUNDAMENTALS_WATCH_LIST_DATA

STR_DATA_BASE_FILE_NAME: str = STR_SQL_DATA_BASE_NAME

STR_DATA_BASE_DIR_NAME: str = STR_SQL_DATA_DIR_NAME

STR_DATA_BASE_TABLE_NAME: str = 'fundamentals_watch_list'

STR_DATA_BASE_TABLE_EVAL_NAME: str = STR_DATA_BASE_TABLE_NAME + '_eval'

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 5.0

DATA_BASE_CONNECTION_URI: bool = True

DATA_BASE_FLAG_ADD_DATE: bool = False

DATA_BASE_FLAG_CLEAN_PRECEDED_DATA: bool = False

DATA_BASE_INT_NUMBER_PRECEDED_DATA = 0

LIST_SECTIONS_WATCH_LIST: list[str] = ['TUPLE_FUNDAMENTALS_WATCH_LIST_QUOTE_ISIN',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_TRAILING_EPS',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_FORWARD_EPS',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_TRAILING_PE',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_FORWARD_PE',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_PRICE_TO_EARNING_TO_GROWTH',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_BOOK_VALUE',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_PRICE_TO_BOOK',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_EARNINGS_QUARTERLY_GROWTH',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_GROWTH_TREND',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_TREND',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_CREDIT',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_PROFIT_MARGINS',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_TOTAL_CASH_PER_SHARE',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_QUICK_RATIO',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_DIVIDEND_YIELD',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_PAYOUT_RATIO',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_FIVE_YEAR_AVE_DIVIDEND_YIELD',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_RATIO_DIVIDEND_YIELD',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_EX_DIVIDED_DATE',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_EX_DIVIDED_DELTA_DATE',
                                       'TUPLE_FUNDAMENTALS_WATCH_LIST_ENTERPRISE_TO_REVENUE']

TUPLE_FUNDAMENTALS_WATCH_LIST_QUOTE_ISIN: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.QUOTE_ISIN',
    'quote_isin',
    ('quote_isin', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_TRAILING_EPS: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.TRAILING_EPS',
    'trailing_eps',
    ('trailing_eps', 'REAL'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_FORWARD_EPS: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.FORWARD_EPS',
    'forward_eps',
    ('forward_eps', 'REAL'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_TRAILING_PE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.TRAILING_PE',
    'trailing_pe',
    ('trailing_pe', 'REAL'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_FORWARD_PE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.FORWARD_PE',
    'forward_pe',
    ('forward_pe', 'REAL'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_PRICE_TO_EARNING_TO_GROWTH: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.FORWARD_PE',
    'price_to_earning_to_growth',
    ('price_to_earning_to_growth', 'REAL'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_BOOK_VALUE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.BOOK_VALUE',
    'book_value',
    ('book_value', 'REAL'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_PRICE_TO_BOOK: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.PRICE_TO_BOOK',
    'price_to_book',
    ('price_to_book', 'REAL'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_EARNINGS_QUARTERLY_GROWTH: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.EARNINGS_QUARTERLY_GROWTH',
    'earnings_quarterly_growth',
    ('earnings_quarterly_growth', 'REAL'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_GROWTH_TREND: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.GROWTH_TREND',
    'growth_trend',
    ('growth_trend', 'TEXT'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_TREND: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.SURPRISE_TREND',
    'surprise_trend',
    ('surprise_trend', 'TEXT'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_CREDIT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.SURPRISE_CREDIT',
    'surprise_credit',
    ('surprise_credit', 'INTEGER'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_PROFIT_MARGINS: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.PROFIT_MARGINS',
    'profit_margins',
    ('profit_margins', 'REAL'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_TOTAL_CASH_PER_SHARE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.TOTAL_CASH_PER_SHARE',
    'total_cash_per_share',
    ('total_cash_per_share', 'REAL'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_QUICK_RATIO: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.QUICK_RATIO',
    'quick_ratio',
    ('quick_ratio', 'REAL'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_DIVIDEND_YIELD: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.DIVIDEND_YIELD',
    'dividend_yield',
    ('dividend_yield', 'REAL'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_PAYOUT_RATIO: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.PAYOUT_RATIO',
     'payout_ratio',
     ('payout_ratio', 'REAL'),
     tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_FIVE_YEAR_AVE_DIVIDEND_YIELD: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.FIVE_YEAR_AVE_DIVIDEND_YIELD',
     'five_year_ave_dividend_yield',
     ('five_year_ave_dividend_yield', 'REAL'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_RATIO_DIVIDEND_YIELD: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.RATIO_DIVIDEND_YIELD',
     'ratio_dividend_yield',
     ('ratio_dividend_yield', 'REAL'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_EX_DIVIDED_DATE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.EX_DIVIDED_DATE',
     'ex_dividend_date',
     ('ex_dividend_date', 'INTEGER'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_EX_DIVIDED_DELTA_DATE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.EX_DIVIDED_DELTA_DATE',
     'ex_dividend_delta_date',
     ('ex_dividend_delta_date', 'INTEGER'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_ENTERPRISE_TO_REVENUE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST.ENTERPRISE_TO_REVENUE',
     'enterprise_to_revenue',
     ('enterprise_to_revenue', 'REAL'),
    tuple)

_index_tuple = myTuple.MyTuple

LIST_FUNDAMENTALS_WATCH_LIST_COLUMN_NAMES: list[str] = [TUPLE_FUNDAMENTALS_WATCH_LIST_QUOTE_ISIN[
                                                        _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_TRAILING_EPS[
                                                        _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_FORWARD_EPS[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_TRAILING_PE[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_FORWARD_PE[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_PRICE_TO_EARNING_TO_GROWTH[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_BOOK_VALUE[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_PRICE_TO_BOOK[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_EARNINGS_QUARTERLY_GROWTH[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_GROWTH_TREND[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_TREND[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_CREDIT[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_PROFIT_MARGINS[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_TOTAL_CASH_PER_SHARE[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_QUICK_RATIO[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_DIVIDEND_YIELD[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_PAYOUT_RATIO[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_FIVE_YEAR_AVE_DIVIDEND_YIELD[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_RATIO_DIVIDEND_YIELD[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_EX_DIVIDED_DATE[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_EX_DIVIDED_DELTA_DATE[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_ENTERPRISE_TO_REVENUE[
                                                       _index_tuple.OPTION_NAME]
                                                   ]

DICT_FUNDAMENTALS_WATCH_LIST_DATA: dict = dict.fromkeys(LIST_FUNDAMENTALS_WATCH_LIST_COLUMN_NAMES)

EMPTY_LIST_ENTIRE_ROW: list = ['', None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                               None, None, None, None, None, None, None]

INDEX_PRIMARY_KEY = LIST_FUNDAMENTALS_WATCH_LIST_COLUMN_NAMES.index(TUPLE_FUNDAMENTALS_WATCH_LIST_QUOTE_ISIN[
                                                        _index_tuple.OPTION_NAME])

LIST_SECTIONS_WATCH_LIST_EVAL: list[str] = ['TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_QUOTE_ISIN',
                                            'TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_PRICE_TO_EARNING_TO_GROWTH',
                                            'TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_PRICE_TO_BOOK',
                                            'TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_EARNING_QUARTERLY_GROWTH',
                                            'TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_SURPRISE_CREDIT',
                                            'TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_PROFIT_MARGIN',
                                            'TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_EX_DIVIDEND_DELTA_DATE',
                                            'TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_ABSOLUTE_SCORE']

TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_QUOTE_ISIN: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST_EVAL.QUOTE_ISIN',
    'quote_isin',
    ('quote_isin', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_PRICE_TO_EARNING_TO_GROWTH: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST_EVAL.PRICE_TO_EARNING_TO_GROWTH',
    'price_to_earning_to_growth_credit',
    ('price_to_earning_to_growth_credit', 'INTEGER'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_PRICE_TO_BOOK: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST_EVAL.PRICE_TO_BOOK',
    'price_to_book_credit',
    ('price_to_book_credit', 'INTEGER'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_EARNING_QUARTERLY_GROWTH: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST_EVAL.EARNING_QUARTERLY_GROWTH',
    'earning_quarterly_growth_credit',
    ('earning_quarterly_growth_credit', 'INTEGER'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_SURPRISE_CREDIT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST_EVAL.SURPRISE_CREDIT',
    'surprise_credit',
    ('surprise_credit', 'INTEGER'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_PROFIT_MARGIN: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST_EVAL.PROFIT_MARGIN',
    'profit_margin_credit',
    ('profit_margin_credit', 'INTEGER'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_DIVIDEND_YIELD: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST_EVAL.DIVIDEND_YIELD',
    'dividend_yield_credit',
    ('dividend_yield_credit', 'INTEGER'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_PAYOUT_RATIO: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST_EVAL.PAYOUT_RATIO',
    'payout_ratio_credit',
    ('payout_ratio_credit', 'INTEGER'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_RATIO_DIVIDEND_YIELD: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST_EVAL.RATIO_DIVIDEND_YIELD',
    'ratio_dividend_yield_credit',
    ('ratio_dividend_yield_credit', 'INTEGER'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_EX_DIVIDEND_DELTA_DATE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST_EVAL.EX_DIVIDEND_DELTA_DATE',
    'ex_divident_delta_date',
    ('ex_divident_delta_date', 'INTEGER'),
    tuple)

TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_ABSOLUTE_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('FUNDAMENTALS_WATCH_LIST_EVAL.ABSOLUTE_SCORE',
    'absolute_score_eval',
    ('absolute_score_eval', 'REAL'),
    tuple)

LIST_DERIVATE_WATCH_LIST_EVAL_COLUMN_NAMES: list[str] = [TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_QUOTE_ISIN[
                                                        _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_PRICE_TO_EARNING_TO_GROWTH[
                                                        _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_PRICE_TO_BOOK[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_EARNING_QUARTERLY_GROWTH[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_SURPRISE_CREDIT[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_PROFIT_MARGIN[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_DIVIDEND_YIELD[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_PAYOUT_RATIO[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_RATIO_DIVIDEND_YIELD[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_EX_DIVIDEND_DELTA_DATE[
                                                       _index_tuple.OPTION_NAME],
                                                   TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_ABSOLUTE_SCORE[
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

LIST_PRICE_TO_EARNING_TO_GROWTH: list[tuple[float, int]] = [
    (0.0001, 5),
    (0.25, 4),
    (0.5, 3),
    (0.75, 2),
    (1, 1),
    (2, 0),
    (5, -1),
    (10, -2),
    (15, -3),
    (20, -4),
    (1000, -5)
]

LIST_PRICE_TO_BOOK: list[tuple[float, int]] = [
    (0.0001, 5),
    (0.1, 4),
    (0.25, 3),
    (0.5, 2),
    (0.75, 1),
    (1, 0),
    (2, -1),
    (5, -2),
    (10, -3),
    (50, -4),
    (1000, -5)
]

LIST_EARNING_QUARTERLY_GROWTH: list[tuple[int, int]] = [
    (50, 5),
    (30, 4),
    (20, 3),
    (10, 2),
    (5, 1),
    (0, 0),
    (-5, -1),
    (-10, -2),
    (-20, -3),
    (-30, -4),
    (-50, -5)
]

LIST_PROFIT_MARGIN: list[tuple[float, int]] = [
    (0.5, 5),
    (0.4, 4),
    (0.3, 3),
    (0.2, 2),
    (0.1, 1),
    (0.01, 0),
    (-0.05, -1),
    (-0.1, -2),
    (-0.3, -3),
    (-1, -4),
    (-100, -5)
]

LIST_DIVIDEND_YIELD: list[tuple[float, int]] = [
    (20, 5),
    (15, 4),
    (10, 3),
    (5, 2),
    (2.5, 1),
    (1, 0),
    (0.5, -1),
    (0.25, -2),
    (0.1, -3),
    (0.05, -4),
    (0.0, -5)
]

LIST_PAYOUT_RATIO: list[tuple[float, int]] = [
    (5, 5),
    (2.5, 4),
    (1, 3),
    (0.75, 2),
    (0.5, 1),
    (0.25, 0),
    (0.1, -1),
    (0.075, -2),
    (0.05, -3),
    (0.01, -4),
    (0.0, -5)
]

LIST_RATIO_DIVIDEND_YIELD: list[tuple[float, int]] = [
    (1.5, 2),
    (1, 5),
    (0.75, 4),
    (0.5, 3),
    (0.25, 1),
    (0.1, 0),
    (0.075, -1),
    (0.05, -2),
    (0.025, -3),
    (0.01, -4),
    (0.001, -5)
]

LIST_EX_DIVIDEND_DELTA_DATE: list[tuple[float, int]] = [
    (365, 0),
    (50, 1),
    (40, 2),
    (30, 3),
    (20, 4),
    (1, 5),
    (-365, 0)
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
]
