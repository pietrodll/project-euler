from math import sqrt

def load_from_file(filename):
    file = open(filename, 'r')
    L = []
    for line in file:
        L += [int(num) for num in line.split(' ')]
    return L

def line_from_index(i):
    return int((sqrt(8*i + 1) - 1) / 2)

def left_child(i):
    return line_from_index(i) + i + 1

def right_child(i):
    return left_child(i) + 1

def right_parent(i):
    line = line_from_index(i)
    p = i - line
    if line_from_index(p) != (line - 1):
        return None
    return p

def left_parent(i):
    line = line_from_index(i)
    p = i - line - 1
    if p < 0 or line_from_index(p) != (line - 1):
        return None
    return p

def max_paths(L):
    M = [0] * len(L)
    M[0] = L[0]

    # fill the triangle at the two extremities
    l = left_child(0)
    r = right_child(0)
    while r < len(L) and l < len(L):
        M[l] = L[l] + M[right_parent(l)]
        M[r] = L[r] + M[left_parent(r)]
        l = left_child(l)
        r = right_child(r)
    
    # fill the rest of the triangle
    for i in range(len(L)):
        l = left_parent(i)
        r = right_parent(i)
        if l is not None and r is not None:
            M[i] = L[i] + max(M[l], M[r])
    
    return M

def max_path_to_bottom(L):
    M = max_paths(L)
    last_line = line_from_index(len(L) - 1)
    first_of_last_line = last_line * (last_line + 1) // 2
    m = M[first_of_last_line]
    for i in range(first_of_last_line, len(L)):
        if M[i] > m:
            m = M[i]
    return m

L = load_from_file('p067_triangle.txt')

print(max_path_to_bottom(L))