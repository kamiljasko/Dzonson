def sort_by_guide(arr, guide):
    output = []
    for i in range(len(arr)):
        output.append('*')
    for number_index in range(len(arr)):
        if guide[number_index] == -1:
            output[number_index] = arr[number_index]
        else:
            output[guide[number_index]-1] = arr[number_index]
    print(output)




if __name__ == '__main__':
    assert(sort_by_guide([56, 78, 3, 45, 4, 66, 2, 2, 4], [3, 1, -1, -1, 2, -1, 4, -1, 5]) ==
                       [78, 4, 3, 45, 56, 66, 2, 2, 4])
    assert(sort_by_guide([45, 56, 78], [-1, 2, 1]) == [45, 78, 56])
    assert(sort_by_guide([2, 5, 3, 1, 4, 70, 8], [2, 5, 1, 3, -1, 4, -1]) == [3, 2, 1, 70, 4, 5, 8])
    assert(sort_by_guide([700, 800, 400, 100, 900, 325], [2, -1, 1, -1, 3, -1]) ==
                       [400, 800, 700, 100, 900, 325])
    assert(
        sort_by_guide([70, 10, 15, 800, 400, 4, 225, 438, 509, 1000], [6, 1, 4, -1, -1, 2, -1, -1, 5, 3]) ==
        [10, 4, 1000, 800, 400, 15, 225, 438, 509, 70])
    assert(sort_by_guide([27, 67, 80, 38, 21], [2, 5, 3, 1, 4]) == [38, 27, 80, 21, 67])
    assert(sort_by_guide([20], [-1]) == [20])