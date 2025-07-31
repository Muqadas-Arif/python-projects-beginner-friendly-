# #project 1 guess random word
import random
target=random.randint(1,50)
while True:
    userchoice=input("enter your choice or press (Q) to quit")
    if userchoice=="q":
        break
    userchoice=int(userchoice)
    if(userchoice==target):
        print('target successful')
        break
    elif(userchoice>target):
        print('num too big try again')
    else:
        print('num too small try again')

print('____GAME OVER____')

#project 2 random pass generator
import random
import string
pass_value=string.ascii_letters + string.digits + string.punctuation
password=''
for i in range(1,11):
    password+=random.choice(pass_value)
print( 'your password id ',password)




