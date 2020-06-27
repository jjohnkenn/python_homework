allow_run = True
    while allow_run:
        allow_run = input("do you want to continue press y \n") == 'y'

age = int(input("enter your age to check if you are eligible for voting \n"))
if age < 18:
    print("Not eligible to vote", age)

else:
    print('you are eligible to vote')
allow_run = input("do you want to continue press y \n") == 'y'
