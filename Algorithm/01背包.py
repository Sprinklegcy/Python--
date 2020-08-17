#  @data   2019/11/30 20:40

"""
    有n个物品，它们有各自的体积和价值，现有给定容量的背包，如何让背包里装入的物品具有最大的价值总和？
    为方便讲解和理解，下面讲述的例子均先用具体的数字代入，即：eg：number＝4，capacity＝8

    i（物品编号）	1	2	3	4
    w（体积）	2	3	4	5
    v（价值）	3	4	5	6
"""
capacity = 8
number = 4
result = [0 for i in range(5)]
w = [0, 2, 3, 4, 5]
v = [0, 3, 4, 5, 6]
dp = [[0 for i in range(9)] for i in range(5)]   # numpy


def knapsack():
    for i in range(1, 5):
        for j in range(1, 9):
            if j < w[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])


def trace_back():
    c = capacity
    for i in range(1, 5):
        if dp[i][c] == dp[i-1][c]:
            result[i] = 0
        else:
            result[i] = 1
            c -= w[i]


knapsack()
trace_back()

print(dp)
del result[0]
print(result)
