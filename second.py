#lists

#lists start from 0. to access last element use -1
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

#to change values
bicycles[0]= 'montra'
print(bicycles)

#append and pop adds and removes last time in list
lastelem = bicycles.pop()
print(bicycles)
bicycles.append('specialized')
#insert and remove
del bicycles[1]
bicycles.insert(1,'cannondale')

#slicing a list from 1 till 3 so 1 and 2 are printed
print(bicycles[1:3])


clone_bicycle=bicycles#copy by reference both point to same object

copy_bicycle=bicycles[:]#copy by values they are now diff objects


#remove based on the element value instead of index
bicycles.remove('montra')




length = len(bicycles)

bicycles.sort(reverse=True)

bicycles.reverse()



magicians = ['alice', 'david', 'carolina']
for magician in magicians:
   print(f"{magician.title()}, that was a great trick!")

#1 to 10 increement by 2, so all odd numbers are prointed. If 2 is omitted in argument then increemented by 1
for value in range(1, 10,2):
    print(value)
    
squares = [value**2 for value in range(1, 11)]
print(squares)


#tuples are like lists but immutable. we can use for statement just like list
my_tup = (1,3,5,66,7,66,3,3,3,66,3)

#my_tup[0] =44 will not work as its immutable
print(f"Last but one value is {my_tup[-2]}")
print(f"results count {my_tup.count(3)}")
#in and not in used as a boolean expression
if magicians:#if magicians not empty
  if('ramu' not in magicians):
    print(" not a magician")    

samp_list=list(range(1,10))
samp_tuple=tuple(range(2,33))
