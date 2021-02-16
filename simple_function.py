
def prefix_average(S):
    n = len(S)
    A = [0]*n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += S[i]
            print(total)
        A[j] = total / (j+1)
        print(A[j])
    return A


test = [1, 4]

print(prefix_average(test))


def addition(s):

    return
