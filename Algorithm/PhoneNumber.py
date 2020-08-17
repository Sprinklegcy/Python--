num = input()
s = set(num)  # 去重

arr = sorted(s, reverse=True)  # 排序 得到第一行结果为一个列表


answers = list()

for e in num:  # 得到第二行结果
    answers.append(arr.index(e))  # 得到当前号码在arr中的下标

res_1 = ''
res_2 = ''
for i in arr:  # 转换为指定格式
    if i != arr[-1]:
        res_1 = res_1 + i + ','
    else:
        res_1 = res_1 + i

res_2 = str(answers).replace(' ', '')
res_2 = res_2.replace('[', '')
res_2 = res_2.replace(']', '')

print("int[] arr = new int[]{" + res_1 + "};")
print("int[] index = new int[]{" + res_2 + "};")