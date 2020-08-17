stack = list()  # 列表模拟栈
stack_order = list()


def lower_bound(arr, aim, start, end):  # 返回第一个大于等于aim的元素下标
    mid = 0
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= aim:
            end = mid
        else:
            start = mid + 1
    return start


def push(key):  # 入栈
    stack.append(key)
    if len(stack_order) == 0:
        stack_order.append(key)
    else:
        if key > stack_order[-1]:
            stack_order.append(key)
        else:
            index = lower_bound(stack_order, key, 0, len(stack_order)-1)
            stack_order.insert(index, key)


def pop():  # 出栈
    if len(stack) == 0:
        return 'Invalid'
    else:
        out = stack.pop()
        index = lower_bound(stack_order, out, 0, len(stack_order) - 1)
        del stack_order[index]
        return out


def peek_median():  # 取中
    length = len(stack_order)
    if length == 0:
        return 'Invalid'
    else:
        if length % 2 == 0:
            return stack_order[length // 2 - 1]
        if length % 2 == 1:
            return stack_order[length // 2]


num = int(input())
answers = list()

for i in range(num):
    command = input().split(' ')  # 用空格分割
    if command[0] == 'Push':
        push(int(command[1]))  # 入栈
    if command[0] == 'Pop':
        answers.append(pop())
    if command[0] == 'PeekMedian':
        answers.append(peek_median())

for e in answers:
    print(e)
