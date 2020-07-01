#233
counter = 0

def fibonacci(n):

    print("fibonacci({})를 구합니다".format(n))
    global counter
    counter += 1

    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n-2)

fibonacci(10)
print("---")
print("fibonachi(10) {}번활용".format(counter))