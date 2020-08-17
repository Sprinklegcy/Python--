import math

num = int(input())

answers = list()

for i in range(num):
    n = int(input())
    if n < 2:
        answers.append('No')
        continue
    flag = 0
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j is 0:
            flag = 1
            break
    if flag is 1:
        answers.append('No')
    else:
        answers.append('Yes')

for e in answers:
    print(e)
