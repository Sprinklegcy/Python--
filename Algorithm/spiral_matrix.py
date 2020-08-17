#  @data   2019/12/2 19:26

"""
 * 1    2   3   4   5
 * 16   17  18  19  6
 * 15   24  25  20  7
 * 14   23  22  21  8
 * 13   12  11  10  9
"""
matrix = [[0 for i in range(1001)] for i in range(1001)]  # 用 0 初始化一个足够大的二维矩阵
N, M = 20, 18
matrix[1][M + 1], matrix[N + 1][M], matrix[N][0] = -1, -1, -1  # 设置自三个点作为边界，也可设置一圈，用于最外圈改变方向
count = 1  # 计数
dr, dc = 0, 1  # dr = [0, 1, 0, -1] 控制方向
# dc = [1, 0, -1, 0]
i, j = 1, 0  # 矩阵索引  从matrix[1][0]开始
num = N * M  # 算出所求螺旋矩阵的元素个数（代码外提）
while count <= num:
    if matrix[i + dr][j + dc] == 0:
        matrix[i + dr][j + dc] = count  # 赋值
        count += 1
        i += dr  # 进入下一个点
        j += dc
    else:
        dr, dc = dc, -dr  # 依次改变方向 注意c++ 和python在此处的区别

for i in range(1, N + 1):  # 输出螺旋矩阵
    for j in range(1, M + 1):
        print(matrix[i][j], end="\t\t")
    print()
