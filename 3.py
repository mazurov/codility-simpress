# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


def solution(K, A):
    # write your code in Python 2.7
    A.sort()
    low, high = 0, len(A) - 1
    result = 0
    while low <= high:
        summa = A[low] + A[high]
        if summa == K:
            result += 2 if low != high else 1

        if summa <= K:
            low += 1
        else:
            high -= 1
    return result

print solution(6, [1, 8, -3, 0, 1, 3, -2, 4, 5])
