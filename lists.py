
# day-5 introduction to lists 
L1=list()
print(len(L1))
fruit=['bannana','apple','orange','pineapple','mango']
print('fruit',fruit,'\nlength',len(fruit))


#Lists can have items of different data types
L3=['s','a',{'apple':'juice','bannana':'shake'},1,2,3]
print(L3)
print(L3[0])
print(L3[2])
print(L3[len(L3)-1])
lst = ['item','item2','item3', 'item4', 'item5']
first,second,*rest=lst
print(first)
print(rest)
print('first 3 fruits\n',fruit[0:3])
print('all fruits\n',fruit[0:])
print('2 and 3 fruits\n',fruit[1:3])
print('first and 4 fruits\n',fruit[::3])

# modify List 
fruit[0]='melon'
print(fruit)
h='bannana' in fruit
print(h)
fruit.append('bannana')
print(fruit)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') 
print(fruits) 
fruits.remove('apple')
print(fruits)
fruits.pop(-3)
print(fruits)


lst = ['item1', 'item2']
del lst[0] 
del lst      
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       
del fruits[1]
print(fruits)       
del fruits[1:3]     
print(fruits) 
del fruits




lst = ['item1', 'item2']
lst.clear()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)
lst = ['item1', 'item2']
lst_copy = lst.copy()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()


fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) 





#Exercise 2

ages1 = [19, 22, 19, 24, 20, 25, 26,2, 24, 25, 24]

ages1.sort()
print(ages1)
Li=ages1
print('min', ages1[0])
print('max',ages1[-1])
Li.insert(0,ages1[0])
Li.insert(-1,ages[-1])
print(Li)
avg=sum(ages1)
print('avg',avg/len(ages1))
ran=Li[-1]-Li[0]
print('ranges',ran)
length1=len(ages1)
print(length1)
if length1%2==0:
    med=ages[length1/2]
    print('median',me)
else:
    a=length1+1
    med1=ages[a//2]
    med2=ages[(length1-1)//2]
    print('median',med1,med2)
