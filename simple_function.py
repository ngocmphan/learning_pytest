
def prefix_average(S):
    n = len(S)
    A = [0]*n
    for j in range(n):
        total = 0
        print(j)
        for i in range(j+1):
            print(i)
            total += S[i]
        A[j] = total / (j+1)
    return A


def prefix_average_2(s):
    """Return list such that, for all j,
    A[j]  equals average of s[0], ....s[j]"""
    n = len(s)
    A = [0]*n
    for j in range(n):
        A[j] = sum(s[0:j+1]) / (j+1)
    return A


def addition(s):
    """Return a list such that, for all j,
    A[j] equals the sum of previous values s[0:j]"""
    n = len(s)
    a = [0]*n
    for j in range(n):
        a[j] = sum(s[0:j+1])
    return a
