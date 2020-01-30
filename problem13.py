def load_numbers(filename):
    file = open(filename, 'r')
    L = []
    for num in file:
        L.append(int(num))
    return L

nums = load_numbers('p013_numbers.txt')

print(nums)
print(sum(nums))