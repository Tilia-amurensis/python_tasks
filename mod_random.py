import random
print(random.randint(1,100))
print(random.randint(50,500))
print(random.randint(100,1000))

num = random.randint(1, 150)
while True:
    print('guess number')
    guess = input()
    i = int(guess)
    if i == num:
        print('Right')
        break
    elif i< num:
        print('Numder higher then you say')
    elif i> num:
        print('Number less then you say')

desserts = ['chocolate','fruits','cookies','cake','jelly']
print(random.choice(desserts))
random.shuffle(desserts)
print(desserts)