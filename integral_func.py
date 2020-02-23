print(abs(10))
print(abs(-10))

steps = -3
if abs(steps)>0:
    print('He is moving')

steps = -2
if steps>0 or steps<0:
    print('He is moving')

year = input('Age:')
if not bool(year.rstrip()):
    print('enter age')

f=['this','is','short','list']
d=dir(f)
print(d)

popcorn = 'I love popcorn'
dir(popcorn)
print(dir(popcorn))

help(popcorn.upper)

eval('print(10*5)')

your_calc=input('Enter math expression:')
print(eval(your_calc))

my_small_program='''print('sandwich')
print('with cheese')'''
exec(my_small_program)

b=float('12')
print(b)

your_age = input('Enter age:')
age = float(your_age)
if age>30:
    print('Your age is higher on %s then we need' % (age-30))

a=int(123.0)
print(a)

c=len('crakazamka')
print(c)

creature_list=['bob','kob','pop']
print(len(creature_list))

products={'chocolate':'tea','milk':'pork','cheese':'banana'}
print(len(products))

fruit=['banana','orange','lemon','carambol']
lentgh=len(fruit)
for x in range(0,lentgh):
    print('there is fruit with index %s:%s' % (x, fruit[x]))

numbers=[5,10,3]
print(max(numbers))
print(min(numbers))

strings='StringD'
print(max(strings))

print(max(6,7,9,111))

guess_num=34
player_guess=[3,67,90,2]
if max(player_guess)>guess_num:
    print('You lose')
else:
    print('You win')

count_by_twos=list(range(0,30,2))
print(count_by_twos)

count_down_by_tows=list(range(40,6,-2))
print(count_down_by_tows)

list_of_numbers=list(range(0,500,50))
print(list_of_numbers)
print(sum(list_of_numbers))


a=abs(-10)+abs(10)
print(a)
b=abs(-10)+abs(-10)
print(b)


