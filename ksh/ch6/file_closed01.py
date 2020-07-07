try:
    # 파일을 엽니다
    file = open("info.txt", "w")
    file.close()
except Exception as e:
    print(e)

print("# 파일이 제대로 닫혔는지 확인")
print("file.closed:", file.closed)