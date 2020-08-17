num = int(input())

mult = '1'

while True:
    remainder = int(mult) % num
    if remainder == 0:
        print(str(int(mult) // num) + ' ' + str(len(mult)))
        break
    else:
        mult = mult + '1'
