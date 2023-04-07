#Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)
j=0
print('with while loop',sep='\n')
while j<11:
    print(j)
    j=j+1
    
#Iterate 10 to 0 using for loop, do the same using while loop.
print('with for loop',sep='\n')
k=10
for i in range(11):
    print(k-i)
print('with while loop',sep='\n')
while k>=0:
    print(k)
    k=k-1
    
#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(1,7):
    for j in range(1,i):
        print('*', end='')
    print('\n')
#print table
num=3;
for i in range(1,11):
    print(f'{num} x {i} ={num*i}')
# print all entry of list

lists=['Python', 'Numpy','Pandas','Django', 'Flask'] 
for list in lists:
    print(list)

#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum=0
for i in range(101):
    sum=sum+i
print(sum)
    
