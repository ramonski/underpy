# -*- coding: utf-8 -*-

__author__ = 'Ramon Bartl <ramon.bartl@googlemail.com>'
__docformat__ = 'plaintext'


import types


def fail(error):
    """ Raises a RuntimeError with the given error Message

        >>> fail("This failed badly")
        Traceback (most recent call last):
        ...
        RuntimeError: This failed badly
    """
    raise RuntimeError(error)


def isString(thing):
    """ checks if an object is a string/unicode type

        >>> isString("")
        True
        >>> isString(u"")
        True
        >>> isString(str())
        True
        >>> isString(unicode())
        True
        >>> isString(1)
        False
    """
    return type(thing) in types.StringTypes


def isList(thing):
    """ checks if an object is a list type

        >>> isList([])
        True
        >>> isList(list())
        True
        >>> isList("[]")
        False
        >>> isList({})
        False
    """
    return type(thing) is types.ListType


def isTuple(thing):
    """ checks if an object is a tuple type

        >>> isTuple(())
        True
        >>> isTuple(tuple())
        True
        >>> isTuple("()")
        False
        >>> isTuple([])
        False
    """
    return type(thing) is types.TupleType


def isDict(thing):
    """ checks if an object is a dictionary type

        >>> isDict({})
        True
        >>> isDict(dict())
        True
        >>> isDict("{}")
        False
        >>> isDict([])
        False
    """
    return type(thing) is types.DictType


def isDigit(thing):
    """ checks if an object is a digit

        >>> isDigit(1)
        True
        >>> isDigit("1")
        True
        >>> isDigit("a")
        False
        >>> isDigit([])
        False
    """
    return str(thing).isdigit()


def toInt(thing):
    """ coverts an object to int

        >>> toInt(1)
        1
        >>> toInt("1")
        1
        >>> toInt("a")
    """
    return isDigit(thing) and int(thing) or None


def toString(thing):
    """ coverts an object to string

        >>> toString(1)
        '1'
        >>> toString([])
        '[]'
        >>> toString(u"a")
        'a'
    """
    return str(thing) or None


def convert(value, converter, default=None):
    """ Converts a value with a given converter function.

        >>> convert("1", toInt)
        1
        >>> convert("a", toInt, 0)
        0
    """
    if not callable(converter): fail("Converter must be a function")
    return converter(value) or default


def pluck(col, key, default=None):
    """ Extracts a list of values from a collection of dictionaries

        >>> stooges = [{"name": "moe",   "age": 40},
        ...            {"name": "larry", "age": 50},
        ...            {"name": "curly", "age": 60}]
        >>> pluck(stooges, "name")
        ['moe', 'larry', 'curly']

        Also works with directly on a dictionary

        >>> curly = stooges.pop()
        >>> pluck(curly, "age")
        [60]
    """
    if not isList(col): col = [col]
    def _block(dct):
        if not isDict(dct): return []
        return dct.get(key, default)
    return map(_block, col)


def pick(dct, *keys):
    """ Returns a copy of the dictionary filtered to only have values for the
        whitelisted keys (or list of valid keys)

        >>> pick({"name": "moe", "age": 50, "userid": "moe1"}, "name", "age")
        {'age': 50, 'name': 'moe'}

    """
    copy = dict()
    for key in keys:
        if key in dct.keys(): copy[key] = dct[key]
    return copy


def omit(dct, *keys):
    """ Returns a copy of the dictionary filtered to omit the blacklisted keys
        (or list of keys)

        >>> omit({"name": "moe", "age": 50, "userid": "moe1"}, "userid", "age")
        {'name': 'moe'}
    """
    copy = dict()
    for key in dct:
        if key not in keys: copy[key] = dct[key]
    return copy


def rename(dct, mapping):
    """ Rename the keys of a dictionary with the given mapping

        >>> rename({"a": 1, "BBB": 2}, {"a": "AAA"})
        {'AAA': 1, 'BBB': 2}
    """

    def _block(memo, key):
        if key in dct:
            memo[mapping[key]] = dct[key]
            return memo
        else:
            return memo
    return reduce(_block, mapping, omit(dct, *mapping.keys()))


def alias(col, mapping):
    """ Returns a collection of dictionaries with the keys renamed according to
        the mapping

        >>> libraries = [{"isbn": 1, "ed": 1}, {"isbn": 2, "ed": 2}]
        >>> alias(libraries, {"ed": "edition"})
        [{'edition': 1, 'isbn': 1}, {'edition': 2, 'isbn': 2}]

        >>> alias({"a": 1}, {"a": "b"})
        [{'b': 1}]
    """
    if not isList(col): col = [col]
    def _block(dct):
        return rename(dct, mapping)
    return map(_block, col)


def first(lst, n=None):
    """ get the first element of a list

        >>> lst = [1, 2, 3, 4, 5]
        >>> first(lst)
        1
        >>> first(lst, 3)
        [1, 2, 3]
    """
    if not isList(lst): return None
    return n is None and lst[0] or lst[0:n]


if __name__ == '__main__':
    import doctest
    doctest.testmod(raise_on_error=False, optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)

# vim: set ft=python ts=4 sw=4 expandtab :
