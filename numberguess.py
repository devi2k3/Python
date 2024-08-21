import random
range=input('Enter a numbee : ')

if range.isdigit():
    range=int(range)
    if range<=0:
        print('please type a number large than o next time. ')
        quit()
else:
    print("please type a number next time.")  
    quit()    
random_num=random.randint(0,range)
guesses=0
while True:
    guesses+=1
    user_guess =input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('please type a number next time')
        continue
    if user_guess==random_num:
        print('YOU GOT IT')
        break
    elif user_guess>random_num:
        print('you were above the number!')
    else:
        print("you are below the number!")
print('you got it in',guesses,'guesses')