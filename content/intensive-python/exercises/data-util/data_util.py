from typing import *

def split(text: str, delim=",") -> List[str]:
    """Return a list of fields in text separated by delim.

    Parameters:
    text: str -- the string to split into fields

    Return:
    List[str] of fields in text

    Usage examples:
    >>> split("foo, bar, baz")
    ['foo', ' bar', ' baz']
    """
    fields = []
    begin = 0
    end = text.find(delim, begin)
    while end != -1:
        fields.append(text[begin:end])
        # Move begin to first index of next field
        begin = end + 1
        end = text.find(delim, begin)
    # After loop finishes, begin points to first index after last delim,
    # or 0 if there were no delims in text.  Add last field.
    fields.append(text[begin:])
    return fields

def zip(xs: Sequence, ys: Sequence) -> Sequence[Tuple]:
    """Return [(x0, y0), ..., (xn, yn)] where n is 1 - min(len(xs), len(ys))

    Parameters:
    xs: Sequence -- the "left" list
    ys: Sequence -- the "right list

    Return:
    Sequence[Tuple] of pairs of corresponding elements in xs and yx

    Usage examples:
    >>> zip(['a', 'b', 'c', 'd'], [1,2,3])
    [('a', 1), ('b', 2), ('c', 3)]
    """
    result = []
    shortest_len = min(len(xs), len(ys))
    for i in range(shortest_len):
        result.append((xs[i], ys[i]))
    return result

def zip_with_indexes(xs: Sequence) -> Sequence[Tuple[int, Any]]:
    """Return [(0, x0), ..., (n, xn)] where n is 1 - len(xs)

    Parameters:
    xs: Sequence -- a sequence

    Return:

    List[Tuple[int, Any]] of pairs of indexes in xs and values at
    corresponding index

    Usage examples:
    >>> zip_with_indexes(['a', 'b', 'c', 'd'])
    [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
    """
    result = []
    for i in range(len(xs)):
        result.append((i, xs[i]))
    return result

def lookup_keys(v: Any, d: Dict) -> Sequence[Any]:
    """Return list of keys in dict d which map to value

    Parameters:
    v: Any -- a value which may be in dictionary d
    d: dict -- a dictionary which may contain the value v

    Return:
    Sequence[Any] of all keys in d that map to v

    Usage examples:
    >>> lookup_keys(1, {'a': 1, 1: 'b', 'c': 2, 'd': 1})
    ['a', 'd']
    """
    result = []
    for key, value in d.items():
        if value == v:
            result.append(key)
    return result
