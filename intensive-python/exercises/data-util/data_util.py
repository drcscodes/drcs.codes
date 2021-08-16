def split(text, delim=","):
    """Return a list of fields in text separated by delim.

    Parameters:
    text: str -- the string to split into fields

    Return:
    list[str]

    Usage examples:
    >>> split("foo, bar, baz")
    ['foo', ' bar', ' baz']
    """
    fields = []
    begin = 0
    end = text.find(delim)
    while True:
        if end == -1:
            fields.append(text[begin:])
            break
        fields.append(text[begin:end])
        begin = end + 1
        end = text.find(delim, end + 1)
    return fields

def zip(xs, ys):
    """Return [(x0, y0), ..., (xn, yn)] where n is 1 - min(len(xs), len(ys))

    Parameters:
    xs: Sequence -- the "left" list
    ys: Sequence -- the "right list

    Return:
    list[tuple]

    Usage examples:
    >>> zip(['a', 'b', 'c', 'd'], [1,2,3])
    [('a', 1), ('b', 2), ('c', 3)]
    """
    result = []
    for i in range(min(len(xs), len(ys))):
        result.append((xs[i], ys[i]))
    return result

def zip_with_indexes(xs):
    """Return [(0, x0), ..., (n, xn)] where n is 1 - len(xs)

    Parameters:
    xs: Sequence -- a sequence

    Return:
    list[tuple]

    Usage examples:
    >>> zip_with_indexes(['a', 'b', 'c', 'd'])
    [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
    """
    result = []
    for i in range(len(xs)):
        result.append((i, xs[i]))
    return result

def lookup_key(v, d):
    """Return a key in dict d which maps to v, or None if v isn't present

    Parameters:
    v: Any -- a value which may be in dictionary d
    d, : dict -- a dictionary which may contain the value v

    Return:
    Any

    Usage examples:
    >>> lookup_key(1, {'a': 1, 1: 'b', 'c': 2})
    'a'
    """
    for key, value in d.items():
        if value == v:
            return key
    return None

def lookup_keys(v, d):
    """Return list of keys in dict d which map to value

    Parameters:
    v: Any -- a value which may be in dictionary d
    d, : dict -- a dictionary which may contain the value v

    Return:
    list[Any]

    Usage examples:
    >>> lookup_keys(1, {'a': 1, 1: 'b', 'c': 2, 'd': 1})
    ['a', 'd']
    """
    result = []
    for key, value in d.items():
        if value == v:
            result.append(key)
    return result
