#  @data   2019/11/30 21:56

x = 'ABCBDABF'
y = "BDCABA"
dp = [[0 for _ in range(101)] for _ in range(101)]

for i in range(1, len(x) + 1):  # 构造dp数组
    for j in range(1, len(y) + 1):
        if x[i - 1] == y[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i][j - 1]

# i, j = len(x), len(y)
res = list()

string = str()


def all(temp, m, n):  # 求出所有解
    while m != 0 and n != 0:
        if x[m - 1] == y[n - 1]:
            temp = x[m - 1] + temp
            m, n = m - 1, n - 1
        elif dp[m - 1][n] > dp[m][n - 1]:
            m -= 1
        elif dp[m - 1][n] < dp[m][n - 1]:
            n -= 1
        elif dp[m - 1][n] == dp[m][n - 1]:
            all(temp, m - 1, n)
            all(temp, m, n - 1)
            return
    res.append(temp)


all(string, len(x), len(y))
print(res)


# for i in range(len(x) + 1):   # 打印dp数组
#     for j in range(len(y) + 1):
#         print(dp[i][j], end="  ")
#     print()


def traceback(i, j):  # 递归求解
    if i == 0 or j == 0:
        return
    elif x[i - 1] == y[j - 1]:
        traceback(i - 1, j - 1)
        print(x[i - 1], end='  ')
    elif dp[i - 1][j] > dp[i][j - 1]:
        traceback(i - 1, j)
    else:
        traceback(i, j - 1)


traceback(len(x), len(y))
