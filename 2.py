# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


def solution(A):
    # write your code in Python 2.7
    if not A:
        return -1

    M = sum(A) / float(len(A))
    current_max = -1
    current_max_index = -1
    for i, v in enumerate(A):
        deviation = abs(v - M)
        if current_max < deviation:
            current_max = deviation
            current_max_index = i
    return current_max_index
