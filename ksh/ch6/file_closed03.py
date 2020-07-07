try:
    # 파일을 엽니다
    file = open("info.txt", "w")
    예외.발생하라()

except Exception as e:
    print(e)
finally::
    file.close()

print("# 파일이 제대로 닫혔는지 확인")
print("file.closed:", file.closed)