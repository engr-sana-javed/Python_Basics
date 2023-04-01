
# Online Python - IDE, Editor, Compiler, Interpreter
#addition
print(3+2)
#subtraction
print(3-2)
#mul
print(3*2)
#division 
print(3/2)
#floor division
print(3//2)
#power
print(3**2)

#datatypes
#int
print(type(1))
#float
print(type(1.5))
#string
print(type("sana"))
#list
print(type([1, 2, 3]))
#touple
print(type((1,2,3)))
#set
print(type({1,2,3}))
#dict
print(type({'sana':'zeeshan'}))

###some common built in function 
#print('hello , world')
print(len('hello , world'))
#convertion 

print(type(10))
print(type(str(10)))
print(type('10'))
print(type(int('10')))
print(type(10))
print(type(float(10)))
input('enter your name:')

# helping
help('str')

a=min(10,40,5)
print(a)
b=max(23,55,88)
print(b)
c=sum([44,1,22])
print(c)

#variable name 
firstname='Zeeshan'
Lastname='Sardar'
Age=28
married=True
skills=['programming','writing']
data={
    'firstname':'Zeeshan',
    'Lastname':'Sardar',
}
print(data)
print(skills)
print('first name:',len(firstname))
print('first name:',firstname)
print(firstname,Lastname)

name=input('enter your name:')
age=input('enter your age')
print(name)
print(age)


#Day 2: 30 Days of python programming
firstname='sana'
secondname='javed'
country='Ireland'
city='dublin'
age=24
year=1996
married=True
is_light_on=False
a,b,c=4,6,7

print(type(city))
l1=len(firstname)
l2=len(secondname)
print(l1>l2)

r=input('enter radius')
area=3.14*float(r)
print(area)
#Day 3: 30 Days of python programming

#age=24
height=153.1
c=5+7j
a=input('enter base:')
b=input('enter height')
c=int(a)*int(b)
print('area is',c)
a=input('enter side a')
b=input('enter side b')
c=input('enter side c')
area=0.5*float(a)*float(b)*float(c)
print(area)

#Day 3: 30 Days of python programming
import cmath
a=[1,3]
b=[5,6]
slop=(a[1]-b[1])/(a[0]-b[0])
print(slop)

#y = x^2 + 6x + 9
a=1
b=6
c=9
d=2*a
s1=(-b+cmath.sqrt(b**2-4*a*c))/d
s2=(-b-cmath.sqrt(b**2-4*a*c))/d
print(s1,s2)
a=len('python')
b=len('dragon')
print(a==b)
print('on'in 'python')
for num in range(6):
    print(num,1, num**1,num**2,num**3)