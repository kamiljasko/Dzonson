def same_case(a, b):
    if not a.isalpha() or not b.isalpha():
        return -1
    elif a.islower() == b.islower() or a.isupper() == b.isupper():
        return 1
    else:
        return 0


if __name__ == '__main__':
    assert (same_case('C', 'B') == 1)
    assert (same_case('b', 'a') == 1)
    assert (same_case('d', 'd') == 1)
    assert (same_case('A', 's') == 0)
    assert (same_case('c', 'B') == 0)
    assert (same_case('b', 'Z') == 0)
    assert (same_case('\t', 'Z') == -1)
    assert (same_case('H', ':') == -1)
