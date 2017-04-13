def solution(S):
    MAX_VAL = 2**12 - 1
    stack = []
    try:
        for ch in S:
            if ch == '+':
                val = stack.pop() + stack.pop()
            elif ch == '*':
                val = stack.pop() * stack.pop()
            else:
                val = int(ch)

            if val > MAX_VAL:
                return -1
            stack.append(val)
        return stack.pop()
    except IndexError:
        return -1

print solution("")
