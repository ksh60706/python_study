#219

def print_n_times(*values, n=1):

    for i in range(n):

        for value in values:
            print(value)

        print()

print_n_times("안녕하세요","즐거운","파이썬프로그래밍",n=4)