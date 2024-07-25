'''
import random
ran=random.randint(1,10)#8
print(ran)'''


import random
ran=random.randint(1,10)#8
chances=1 
while chances<=3: 
    guess=int(input('enter the number'))
   #ran=guess
    if guess==ran:
        print('congrats')
        break
    else:
        chances+=1 
        continue
if chances>3:
    print('failed try next time')
