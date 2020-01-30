from math import sqrt

tri = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


# 0 -> 1, 2
# 1 -> 3, 4
# 2 -> 4, 5
# 3 -> 6, 7
# 4 -> 7, 8
# 5 -> 8, 9

# L + x + 1, L + x + 2

# S = n(n+1)/2 => n^2 + n - 2S = 0 => n = ( -1 +- sqrt(1 + 8S) ) / 2

# L = int((sqrt(8S+1) - 1)/2)


def load_from_string(string):
    L = []
    lines = string.split('\n')
    for line in lines:
        L += [int(num) for num in line.split(' ')]
    return L

def get_line_from_index(i):
    return int((sqrt(8*i + 1) - 1) / 2)

def get_left_child(i):
    return get_line_from_index(i) + i + 1

def get_right_child(i):
    return get_left_child(i) + 1

# C = L(RP) + RP + 1 = L(C) - 1 + RP + 1 = L(C) + RP ==> RP = C - L(C)

def right_parent(i):
    line = get_line_from_index(i)
    p = i - line
    if get_line_from_index(p) != (line - 1):
        return None
    return p

def left_parent(i):
    line = get_line_from_index(i)
    p = i - line - 1
    if p < 0 or get_line_from_index(p) != (line - 1):
        return None
    return p

def max_paths(L):
    M = [0] * len(L)
    M[0] = L[0]

    # fill the triangle at the two extremities
    l = get_left_child(0)
    r = get_right_child(0)
    while r < len(L) and l < len(L):
        M[l] = L[l] + M[right_parent(l)]
        M[r] = L[r] + M[left_parent(r)]
        l = get_left_child(l)
        r = get_right_child(r)
    
    # fill the rest of the triangle
    for i in range(len(L)):
        l = left_parent(i)
        r = right_parent(i)
        if l is not None and r is not None:
            M[i] = L[i] + max(M[l], M[r])
    
    return M

def test():
    for i in range(10):
        print('Index: {} - LP: {} - RP: {} - LC: {} - RC: {}'.format(i, left_parent(i), right_parent(i), get_left_child(i), get_right_child(i)))


L = load_from_string(tri)

# test()


M = max_paths(L)

def max_path_to_bottom(L):
    M = max_paths(L)
    last_line = get_line_from_index(len(L) - 1)
    first_of_last_line = last_line * (last_line + 1) // 2
    m = M[first_of_last_line]
    for i in range(first_of_last_line, len(L)):
        if M[i] > m:
            m = M[i]
    return m

print(M)
print(max_path_to_bottom(L))