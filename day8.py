def sum(a,b):
    s=a+b
    return s

a1=int(input("enter first num"))
b1=int(input("enter second num"))
print(sum(a1,b1))

#sum of all elements

def add_all_nums(*arg):
    s=0
    for i in arg:
        s=s+i
    return s
print(add_all_nums(1,2,3,4))

#Write a function called calculate_slope which return the slope of a linear equation
def slope(x1,x2,y1,y2):
    if abs(x2-x1)!=0:
        return float((y2-y1)/(x2-x1))

x1 = 4
y1 = 2
x2 = 2
y2 = 5
print(slope(x1,x2,y1,y2))

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import cmath
def quad(a,b,c):
    if a!=0:
        s1=-(b+cmath.sqrt(b*b-4*a*c))/(2*a)
        s2=-(b-cmath.sqrt(b*b-4*a*c))/(2*a)
        return (s1,s2)
print(quad(1,3,4))


#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lis):
    li=len(lis)
    for i in range(li):
        print(lis[i])
    
        
print_list([1,2,3,4])
#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(list1):
    l=len(list1)-1
    while l>=0:
        print(list1[l])
        l=l-1
        
reverse_list([1,2,3,4])

#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    #print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
def evens_and_odds(num):
    if num%2==0:
        print(f'the numbers of odds are {(num-(num//2))} ')
        print(f'the numbers of even are {(num//2)+1}')
    else:
        print(f'the numbers of odds are {num//2}')
        print(f'the numbers of even are {(num//2)}')
evens_and_odds(100)
evens_and_odds(2)
print([1,2,3,4,5,6,7,8,9,10])
    
#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def fac(num):
    s=1;
    while num>1:
        s=s*num;
        num=num-1
    return s
print(fac(1))
print(fac(2))
print(fac(4))
#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(par):
    if len(par)==0:
        return True
    else :
        return False
li2=[]
if is_empty(li2):
    print("its empty")
else:
    print("not empty")
        
        
    