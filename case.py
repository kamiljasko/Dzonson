def same_case(a, b):
#     if type(a) == type(b):
#         return 1
#     elif a.islower() == b.isupper() :
#         return 0
#     elif b.islower() == a.isupper():
#         return 0
#     else:
#         return -1

    # if type(a) == type(b):  tu jest źle bo od razu daje 1 zamiast przechodzić dalej do warunku
    #         return 1
    # elif a.islower() != b.islower() or a.isupper() != b.isupper():
    #         return 0
    # else:
    #     return -1


    # if type(a) == type(b):
    #     return 1
    # elif a.islower() != b.islower():
    #     return 0
    # elif a.isupper() != b.isupper():
    #     return 0
    # else:
    #     return -1
    #


if __name__ == '__main__':
    assert(same_case('C', 'B') == 1)
    assert(same_case('b', 'a') == 1)
    assert(same_case('d', 'd') == 1)
    assert(same_case('A', 's') == 0)
    assert(same_case('c', 'B') == 0)
    assert(same_case('b', 'Z') == 0)
    assert(same_case('\t', 'Z') == -1)
    assert(same_case('H', ':') == -1)
