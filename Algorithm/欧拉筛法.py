#  @data   2020/3/9 19:43

# 埃氏筛法
# isPrime = [True for _ in range(101)]
#
# for i in range(2, len(isPrime)):
#     if isPrime[i]:
#         j = 2
#         while j * i <= 100:
#             isPrime[i * j] = False
#             j += 1
#
#
# result = []
#
# # print(isPrime)
# for num in range(2, len(isPrime)):
#     if isPrime[num]:
#         result.append(num)
#
# print(result)
# print(len(result))
# 欧拉筛法

N = int(input("请输入一个大于2的整数："))
result = set()
isPrime = [True for _ in range(N)]
for i in range(2, N):
    if isPrime[i]:
        result.add(i)
    for e in result:
        if e * i >= N:
            break
        isPrime[e * i] = False
        if i % e == 0:
            break

print(result)

