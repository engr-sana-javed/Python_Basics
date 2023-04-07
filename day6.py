
#condition
'''Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive'''

a=int(input('Enter your age:'))
if a>=18:
    print("You are old enough to learn to drive")
else:
    print(f"You need {18-a} more years to learn to drive",)
    
#exercise2
'''Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
Enter your age: 30
You are 5 years older than me'''

age1=int(input("enter my age:"))
age2=int(input("enter your age:"))
if age1>age2:
    print(f"i am {age1-age2} years older than you")
else:
    print(f"you are {age2-age1} years older than you")
    
# exercise 3
#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a1=int(input("enter 1 number:"))
a2=int(input("enter 2 number:"))
if a1>a2:
    print(f"{a1} is greater than {a2}")
else:
    print(f"{a2} is greater than {a1}")  
 
 #exercise4   
'''Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F'''

a1=int(input("enter your scores:"))
if a1>=80 and a1<=100:
    print("A")
elif a1>=70 and a1<=79:
    print("B")
elif a1>=60 and a1<=69:
    print("C")
elif a1>=50 and a1<=59:
    print("D")
else:
    print("F")
    
    
'''The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
'''
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=input("enTER the name of fruit")
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)
    
'''Here we have a person dictionary. Feel free to modify it!
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:'''

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
a=person.get('skills');
if 'skills' in person:
    a=person.get('skills');
    g=a[(len(a)-1)//2]
    print(g)
if 'Python' in a:
    print(a)
if 'JavaScript' in a and 'React' in a and not('Node' in a):
    print("he is frontend a developer")
elif  'Node' in a and 'Python' in a and 'MongoDB' in a:
    print('He is a backend developer')
else:
    print('no title')
    