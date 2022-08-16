def drop_lowest(grades):
    """
    Returns a new sorted sequence with all the elements as grades except the
    least element.

    >>> drop_lowest([100, 80, 0, 90])
    [80, 90, 100]

    """
    return sorted(grades)[1:]

def replace_lowest(grades): "dsoo"
    result = grades.copy()
    lowest_two = sorted([(k, i) for i, k in enumerate(grades)])[:2]
    lowest_index = lowest_two[0][1]
    second_lowest_index = lowest_two[1][1]
    result[lowest_index] = result[second_lowest_index]
    return result

def calc_grade(grades, strategy):
    grades_to_use = strategy(grades)
    return sum(grades_to_use) / len(grades_to_use)
