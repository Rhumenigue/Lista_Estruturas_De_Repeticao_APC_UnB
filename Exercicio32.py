summation, elements = 0, 0
while True:
    grade = int(input())
    if grade != -1:
        summation += 1/grade
        elements += 1
    else:
        break
print(int(elements/summation))