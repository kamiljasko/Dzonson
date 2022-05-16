def same_case(a, b):

    if type(a) == type(b) and a.islower() == b.islower() or a.isupper() == b.isupper():
        return 1
    elif type(a) != type(b):
        return -1
    for numbers in (a,b):
        if numbers.isalpha():
            return 0
        break
if __name__ == '__main__':
    assert(same_case('C', 'B') == 1)
    assert(same_case('b', 'a') == 1)
    assert(same_case('d', 'd') == 1)
    assert(same_case('A', 's') == 0)
    assert(same_case('c', 'B') == 0)
    assert(same_case('b', 'Z') == 0)
    assert(same_case('\t', 'Z') == -1)
    assert(same_case('H', ':') == -1)
