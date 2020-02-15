def testfunc(myname):
    print ('Hello,%s'%myname)

testfunc('Marry')

def testfunc1(fname,lname):
    print('Hello,%s %s' % (fname, lname))

testfunc1('Vasya', 'Pupkin')

fname = 'kolya'
lname = 'gubkin'
testfunc1(fname,lname)

def savings(pocket_money, paper_route, spending):
    return pocket_money+paper_route - spending
    
print(savings(10,10,5)) 
another_var = 10
def variable_test():
    first_var = 12
    second_var = 16
    return first_var*second_var*another_var

print(variable_test())
print(another_var)

def spaceship_build(cans):
    total_cans=0
    for week in range(1,53):
        total_cans=total_cans+cans
        print('Week %s, cans %s' %(week, total_cans))

spaceship_build(3)

import time
print(time.asctime())

with open('py_if_else.py') as myfile:
    myline = myfile.readline()
    while myline:
        print(myline)
        myline = myfile.readline()


def silly_joke(age):
    if age >=10 and age <=13:
        print('you are so young')
    else:
        print('hohoho')

silly_joke(13)

def moon_weight(lun_weight,rease,year):
    for year in range(year):
        lun_weight = lun_weight*rease
        print('Year %s = %s'% (year, lun_weight))

moon_weight(57, 0.123, 5)

import sys
print('Enter lun weight')
lw = int(sys.stdin.readline())
print('Enter rise')
rs = int(sys.stdin.readline())
print('Enter year')
y = int(sys.stdin.readline())

moon_weight(lw, rs, y)



