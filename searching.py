x = [5, 5, 10, 3, 2, 6, 7]
y1 = 4
y2 = 2

def find_element(x, y):
    for i in x:
        if i == y:
            return x.index(i)
    return 0

print(find_element(x, y1))
print(find_element(x, y2))
