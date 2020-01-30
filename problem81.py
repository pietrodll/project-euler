import numpy as np

example = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]

def load_matrix(filename):
    file = open(filename, 'r')
    matrix = []
    for line in file:
        int_line = [int(x) for x in line.split(',')]
        matrix.append(int_line)
    file.close()
    return matrix

matrix = load_matrix('p081_matrix.txt')

def minimal_path(M):
    n = len(M)
    P = np.inf * np.ones((n, n), dtype=np.int)
    P[0][0] = M[0][0]
    for i in range(1, n):
        P[i][0] = M[i][0] + P[i-1][0]
    for j in range(1, n):
        P[0][j] = M[0][j] + P[0][j-1]
    for i in range(1, n):
        for j in range(1, n):
            P[i][j] = M[i][j] + min(P[i-1][j], P[i][j-1])
    return P

# print(matrix)

# print(minimal_path(matrix))