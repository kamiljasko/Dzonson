def solution(a, b):
    for strings in solution(a, b):
        if len(a) > len(b):
            return b + a
        else:
            return a + b



if __name__ == '__main__':
    assert(solution('45', '1') == '1451')
    assert(solution('13', '200') == '1320013')
    assert(solution('Soon', 'Me') == 'MeSoonMe')
    assert(solution('U', 'False') == 'UFalseU')
