from random import randrange
option = 'yes'
 #if option == 'yes':
while True:
    try:
        a = randrange(10)
        b = randrange(10)
        print(a,"/",b,"=")
        prompt = 'ans : '
        ans = input(prompt)
        if(int(ans) == ((a/b))):
            print("Correct!")
        else:
            print("OOPS!!,Wrong answer!!")
#     except ZeroDivisionError:
#         print("Division by zero error")
    except ValueError:
        print("Integers only please")
    option = input("Do you want to play again?")