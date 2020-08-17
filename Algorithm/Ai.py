import string
 # 部分AC
num = int(input())
questions = list()
answers = list()
while num > 0:
    num = num - 1
    my_str = input()
    questions.append(my_str)
    if my_str.strip() == '':
        answers.append('')
        continue
    arr = list()
    for e in my_str:
        arr.append(e)
    for i in range(len(arr) - 1):
        if arr[i] is ' ' and arr[i + 1] not in string.ascii_letters + string.digits:
            arr[i], arr[i + 1] = '', arr[i + 1]
        else:
            arr[i] = arr[i]
    res = ''  # 去掉标点符号前的空格
    for e in arr:
        res = res + e

    s = ''
    for e in res.split(' '):
        if e is not '':
            s = s + e + ' '
    s = s.rstrip()  # 去掉末尾的一个空格

    result = ''
    for elem in s:
        if elem is not 'I':
            result = result + elem.lower()
        else:
            result = result + elem

    result = result.replace('?', '!')
    result = result.replace("can you", "I can")
    result = result.replace("could you", "I could")

    array = list()
    array.append(result[0])
    for i in range(1, len(result) - 1):
        if result[i - 1] not in string.ascii_letters + string.digits \
                and result[i + 1] not in string.ascii_letters + string.digits and result[i] is 'I':
            array.append('you')
        else:
            array.append(result[i])
    array.append(result[len(result)-1])
    rs = ''
    for e in array:
        rs = rs + e
    res = list()
    for e in rs:
        res.append(e)
    for i in range(1, len(rs) - 2):
        if res[i] is 'm' and res[i + 1] is 'e' and res[i - 1] not in string.ascii_letters \
                and res[i + 2] not in string.ascii_letters:
            res[i], res[i + 1] = 'you', ''
    ss = ''
    for e in res:
        ss = ss + e
    answers.append(ss)

for i in range(len(answers)):
    print(questions[i])
    print('AI: ' + answers[i])