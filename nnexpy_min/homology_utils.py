import random as r


def independent(x, S):
    import numpy as np
    mat = []
    for i in range(len(S[0])):
        temp = []
        for j in range(len(S)):
            temp.append(S[j][i])
        temp.append(x[i])
        mat.append(temp)
    rank = np.linalg.matrix_rank(mat, tol=0.1)
    return rank == len(mat[0])


def findPointStructDimension(pointList, *args, **kwargs):
    import numpy as np
    errorRate = kwargs.get('errorRate', 0.005)
    A = [list(x) for x in pointList]
    B = [A[0]]
    A = A[1:]
    errorCount = 0
    while len(A) > 0 and len(B) < len(B[0]):
        head = A[0]
        A = A[1:]
        if independent(head, B):
            if errorCount < len(pointList) * errorRate:
                errorCount += 1
            else:
                B.append(head)
    return len(B) - 1


def selectRandomSublist(L, s):
    import random as r
    res = []
    for _ in range(s):
        if len(L) - 1 == 0:
            random = 0
        elif len(L) == 0:
            break
        else:
            random = r.randint(0, len(L) - 1)
        a = L.pop(random)
        res.append(a)
    return res
