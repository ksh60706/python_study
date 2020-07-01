#267

def test():
    print("a지점 통과")
    yield 1
    print("b지점 통과")
    yield 2
    print("c지점 통과")

output = test()
print("d지점 통과")
a = next(output)
print(a)
print("e지점 통과")
b = next(output)
print(b)
print("f지점 통과")
c = next(output)
print(c)

next(output)