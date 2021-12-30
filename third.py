#python dictionary similar to json
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print(favorite_languages['jen'])
favorite_languages['kishore']='java'
print(favorite_languages['kishore'])
#use get to obtain a value and return default if not found
print(favorite_languages.get('arshu','papa'))
#note there is no backet in for () like java
for name,lang in favorite_languages.items():
  print(f"name is {name} and lang is {lang}")

for name in favorite_languages.keys():
    print(name)


#since a dictinoary is like a json we can have a json which has a dictionray within dictionary,
#dictionary with liost of values etc.
users = {
       'aeinstein': {
           'first': 'albert',
           'last': 'einstein',
           'location': ['princeton','newjersey'],
           }
}
#users is a dictinary containing dictinary
for username,info in users.items():
  for pos,value in info.items():
      print("pos "+ pos,value)

#use inout to read from stdin  
age = input("what is your age")
age = int(age)
print(age > 48)


current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#this is a list
unconfirmed_users = ['alice', 'brian', 'candace']

while unconfirmed_users:
    print(unconfirmed_users.pop())#pops from end of the list so candice ll be printed first

#storing in a dictionary
responses={};#declare dictionary. note dictionary like a JSON
responses["abc"]="some value"
responses["ged"]="anpother value"

for nam, val in responses.items():
    print(f"name is {nam}")
    

def test_func():
    print("test func invoked")
