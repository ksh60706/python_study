#224

def sum_all(start = 0, end=100, step=1):

    output = 0
    
    for i in range(start, end + 1, step):
        output += i

    return output

print("a", sum_all(0,100, 10))
print("b", sum_all(end = 100))
print("c", sum_all(end = 100, step = 2))