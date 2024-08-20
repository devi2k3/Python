print("Welcome to my computer quiz!")

playing=input("Do you want to play? ")
if playing.lower() !='yes':
    quit()
print("Okay!Let's play :)")
score=0

answer=input("1. What type of language is Python? ")
if answer == "Interpreted":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
answer=input(" 2. What keyword is used to define a function in Python?")
if answer == "def":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
answer=input("3. Which data structure is mutable: List or Tuple? ")
if answer == "List":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
answer=input("4. What symbol is used to start a comment in Python? ")
if answer == "#":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
answer=input("5. Which function is used to output text in Python? ")
if answer == "print":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
answer=input("6. What keyword is used to create a loop in Python? ")
if answer == "for":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
answer=input(" 7. What is the default data type for numbers with a decimal point in Python?")
if answer == "Float":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
answer=input("8. Which method is used to add an element to the end of a list? ")
if answer == "append":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
answer=input("9. What keyword is used to handle exceptions in Python? ")
if answer == "try":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
answer=input("10. Which keyword is used to create a class in Python?")
if answer == "class":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
print("you got",score,"questions correct! ")
print("you Scored",((score/10)*100),"%.")