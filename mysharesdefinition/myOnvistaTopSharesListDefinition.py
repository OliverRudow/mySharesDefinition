"""myOnvistaTopSharesListDefinitions.py."""

__title__: str = "myOnvistaTopSharesListDefinitions"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from mydatabase.mySQLDataBase import STR_SQL_DATA_BASE_NAME, STR_SQL_DATA_DIR_NAME
from mytuple import myTuple

def init_dict_onvista_top_shares_list_data() -> dict[str, str| bool | None]:
    """Initialize the dict to be used to get the static data from yfinance."""
    elem = 0

    for key in DICT_ONVISTA_TOP_SHARES_LIST_DATA:
        DICT_ONVISTA_TOP_SHARES_LIST_DATA[key] = EMPTY_LIST_ENTIRE_ROW[elem]
        elem += 1

    return DICT_ONVISTA_TOP_SHARES_LIST_DATA

STR_DATA_BASE_FILE_NAME: str = STR_SQL_DATA_BASE_NAME

STR_DATA_BASE_DIR_NAME: str = STR_SQL_DATA_DIR_NAME

STR_DATA_BASE_TABLE_NAME: str = 'onvista_top_shares_list'

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 5.0

DATA_BASE_CONNECTION_URI: bool = True

LIST_SECTIONS_WATCH_LIST: list[str] = ['ONVISTA_TOP_SHARES_LIST.QUOTE_ISIN',
                                       'ONVISTA_TOP_SHARES_LIST.QUOTE_SHIFT',
                                       'ONVISTA_TOP_SHARES_LIST.QUOTE_REL_PERF']


TUPLE_ONVISTA_TOP_SHARES_LIST_QUOTE_ISIN: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('ONVISTA_TOP_SHARES_LIST.QUOTE_ISIN',
     'quote_isin',
    ('quote_isin', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_ONVISTA_TOP_SHARES_LIST_QUOTE_SHIFT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ONVISTA_TOP_SHARES_LIST.QUOTE_SHIFT',
     'quote_shift',
    ('quote_shift', 'INTEGER'),
    tuple)

TUPLE_ONVISTA_TOP_SHARES_LIST_QUOTE_REL_PERF: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ONVISTA_TOP_SHARES_LIST.QUOTE_REL_PERF',
     'quote_rel_perf',
    ('quote_rel_perf', 'REAL'),
    tuple)

_index_tuple = myTuple.MyTuple

LIST_ONVISTA_TOP_SHARES_LIST_COLUMN_NAMES: list[str] = [TUPLE_ONVISTA_TOP_SHARES_LIST_QUOTE_ISIN[
                                                            _index_tuple.OPTION_NAME],
                                                        TUPLE_ONVISTA_TOP_SHARES_LIST_QUOTE_SHIFT[
                                                            _index_tuple.OPTION_NAME],
                                                        TUPLE_ONVISTA_TOP_SHARES_LIST_QUOTE_REL_PERF[
                                                            _index_tuple.OPTION_NAME],
                                                            ]

DICT_ONVISTA_TOP_SHARES_LIST_DATA: dict = dict.fromkeys(LIST_ONVISTA_TOP_SHARES_LIST_COLUMN_NAMES)

EMPTY_LIST_ENTIRE_ROW: list = ['', None, None]

INDEX_PRIMARY_KEY = LIST_ONVISTA_TOP_SHARES_LIST_COLUMN_NAMES.index(TUPLE_ONVISTA_TOP_SHARES_LIST_QUOTE_ISIN[
                                                        _index_tuple.OPTION_NAME])
