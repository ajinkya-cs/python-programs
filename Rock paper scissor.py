import random
t =input("Choose Rock Paper or scissors ")
list1=['rock','paper','scissor']
back=random.choice(list1)
print('Your input choice was',t)
print('Computer Choice is',back)
if t== 'rock' and back=='scissor':
    print('You Win')
elif t== 'paper' and back=='rock':
    print('You Win') 
elif t== 'scissor' and back=='paper':
    print('You Win') 
elif t==back:
    print('Tie')
else:
    print('You loose')    
    



