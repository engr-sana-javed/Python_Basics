# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

age = [22, 19, 24, 25, 26, 24, 25, 24]
'''Exercises: Level 1
Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard'''
print(len(it_companies))
it_companies.add('twitter')
print(it_companies)
it_companies.update(['daraz','shein'])
print(it_companies)
it_companies.remove('daraz')
print(it_companies)
it_companies.discard('shein')
print(it_companies)

'''Exercises: Level 2
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely'''
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C=A.union(B)
print(C)
D=A.intersection(B)
print(D)
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))