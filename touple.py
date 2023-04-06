
'''Exercises: Level 1
Create an empty tuple
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members'''


t1=tuple();
s=('sana','saba','sidra')
b=('hamza','sikandar','rustam')
sib=s+b
print(sib)
print(len(sib))
l=list(sib)
l.append('javed')
l.insert(0,'khalida')
fam=tuple(l)
print(fam)

'''Exercises: Level 2
Unpack siblings and parents from family_members
Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Change the about food_stuff_tp tuple to a food_stuff_lt list
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
Slice out the first three items and the last three items from food_staff_lt list
Delete the food_staff_tp tuple completely
Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')'''

fruits=('banana','apple')
animal=('cow',"goat")
vegetables=('onion','tomato')
food_stuff_tp=fruits+animal+vegetables
food_stuff_list=list(food_stuff_tp)
print(len(food_stuff_list))
print(food_stuff_list[len(food_stuff_list)//2:])
print('first three', food_stuff_list[0:3])
print('Last three', food_stuff_list[-3:])
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
f='Iceland' in nordic_countries
print(f)
