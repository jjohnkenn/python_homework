print("==============break function==========")
for i in range(1, 51):
    if i==15:
        break
    print(i)

print("==============continue function==========")
for i in range(1, 51):
        if i in range(1, 25):
            continue
        print(i)

for i in range(1, 51):
    pass

    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    sum_ = float(num1) + float(num2)
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum_))