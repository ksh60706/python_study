def print_t(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)

print_t("안녕","하세요",n=4)