import collections

s = input()
s = s.upper()  # 先转换为大写

for e in s:
    if e not in 'GPLT':
        s = s.replace(e, '')  # 去掉其他字母

dict_c = collections.Counter(s)  # 统计

max_len = 0
for i in dict_c.keys():
    if dict_c[i] > max_len:
        max_len = dict_c[i]  # 获取字母做大个数

answers = ''

for i in range(max_len):
    for e in 'GPLT':
        if s.find(e) != -1:  # 如果剩余字符串中还有这四个字母中的一个
            answers = answers + e  # 放入结果中
            s = s.replace(e, '', 1)  # 删除刚才放入的

print(answers)
