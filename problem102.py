def load_triangles(filename):
    L = []
    try:
        f = open(filename, 'r')
        for line in f:
            coords = line.split(',')
            tri = [(int(coords[2 * i]), int(coords[2 * i + 1])) for i in range(3)]
            L.append(tri)
        return L
    finally:
        f.close()


def vec_prod(x, y):
    return x[0] * y[1] - x[1] * y[0]


def vector(a, b):
    return (b[0] - a[0], b[1] - a[1])


def contains_origin(tri):
    a = vector(tri[0], tri[1])
    b = vector(tri[1], tri[2])
    c = vector(tri[2], tri[0])
    p1 = vec_prod(a, vector(tri[0], (0, 0)))
    p2 = vec_prod(b, vector(tri[1], (0, 0)))
    p3 = vec_prod(c, vector(tri[2], (0, 0)))
    return p1 * p2 >= 0 and p2 * p3 >= 0


# T1 = [(-340,495), (-153,-910), (835,-947)]
# T2 = [(-175,41), (-421,-714), (574,-645)]
# print(contains_origin(T1))
# print(contains_origin(T2))

def count(L):
    c = 0
    for tri in L:
        if contains_origin(tri):
            c += 1
    return c

L = load_triangles('p102_triangles.txt')

print(count(L))