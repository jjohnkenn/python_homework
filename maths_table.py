b = "We are going to study tables"
print(b)
allow_run=True
while allow_run:
    table_input = int(input('enter the number to print the table \n'))

    for table_loop in range(1, 11):
        print(table_input, "x", table_loop, "=", table_input*table_loop, sep="\t")

    allow_run = input("do you want to continue press y \n") == 'y'

print("Thank you for using this application")
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
sum_ = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum_))