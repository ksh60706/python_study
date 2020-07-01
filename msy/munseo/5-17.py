#236

dictionary = {
    1:1,
    2:2
}

def fibonachi(n):
    if n in dictionary:

        return dictionary[n]
    else:

        output = fibonachi(n - 1) + fibonachi(n - 2)
        dictionary[n] = output
        return output

print("fibonachi(10)",fibonachi(10))
print("fibonachi(20)",fibonachi(20))
print("fibonachi(30)",fibonachi(30))
print("fibonachi(40)",fibonachi(40))
print("fibonachi(50)",fibonachi(50))