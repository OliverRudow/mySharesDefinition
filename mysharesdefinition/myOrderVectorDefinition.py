"""myOrderVectorDefinitions.py."""

__title__: str = "myOrderVectorDefinitions"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"


from mytuple import myTuple

TUPLE_ORDER_VECTOR_HEADER: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ORDER_VECTOR.HEADER',
    'header',
    ('header', 'TEXT'),
    tuple)

TUPLE_ORDER_VECTOR_RANKING: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ORDER_VECTOR.RANKING',
    'ranking',
    ('ranking', 'TEXT'),
    tuple)

TUPLE_ORDER_VECTOR_ANALYST: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ORDER_VECTOR.ANALYST',
    'analyst',
    ('analyst', 'TEXT'),
    tuple)

TUPLE_ORDER_VECTOR_DERIVATE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ORDER_VECTOR.DERIVATE',
    'derivate',
    ('derivate', 'TEXT'),
    tuple)

TUPLE_ORDER_VECTOR_FUNDAMENTALS: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ORDER_VECTOR.FUNDAMENTALS',
    'fundamentals',
    ('fundamentals', 'TEXT'),
    tuple)

TUPLE_ORDER_VECTOR_PERFORMANCE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('ORDER_VECTOR.PERFORMANCE',
    'performance',
    ('performance', 'TEXT'),
    tuple)

_index_tuple = myTuple.MyTuple

LIST_ORDER_VECTOR_COLUMN_NAMES: list[str] = [TUPLE_ORDER_VECTOR_HEADER[
                                                _index_tuple.OPTION_NAME],
                                             TUPLE_ORDER_VECTOR_RANKING[
                                                _index_tuple.OPTION_NAME],
                                             TUPLE_ORDER_VECTOR_ANALYST[
                                                _index_tuple.OPTION_NAME],
                                             TUPLE_ORDER_VECTOR_DERIVATE[
                                                _index_tuple.OPTION_NAME],
                                             TUPLE_ORDER_VECTOR_FUNDAMENTALS[
                                                _index_tuple.OPTION_NAME],
                                             TUPLE_ORDER_VECTOR_PERFORMANCE[
                                                _index_tuple.OPTION_NAME]]

