#Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg=[i for i in numbers if i<=0]
print(neg)

#Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

#output
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
l=[number for row in list_of_lists for number in row]
print(l)

r=[(i,1,i,i*2,i*3,i*4,i*5) for i in range(11)]
print(r)

#prime number

def is_prime(num):
    t=True
    if num==0 or num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return t
print(is_prime(2))

# Write a functions which checks if all items are unique in the list.

def unique(list):
    for i in list:
        if list.count(i)>1:
            return False
        else:
            flag=True
    return flag
print(unique([1,4,7,6,1]))

#Write a function which checks if all the items of the list are of the same data type.
print("check same data type")
def samedata(list):
    for i in range(len(list)):
        if i<len(list)-1:
            if type(list[i])==type(list[i+1]):
                flage=True
            else:
                return False
    return flage
list=['d',3,'s','k',3]
print(samedata(list))
#Write a function which check if provided variable is a valid python variable