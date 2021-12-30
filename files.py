with open('car.py') as file_object1:
    contents = file_object1.read()
print(contents)

with open('car.py') as file_object1:
    for lin in file_object1:
        print(lin)

linesfromFile = file_object1.readlines

#here below we open in w write mode. for append use a instead of w.
with open('1.txt','w') as write_obj:
    write_obj.write("its a new file")

try:    
    with open('abc.txt') as read1:
        read1.read()
except:
    print("exception occured")

def count_words(filename):
    try:
        with open(filename) as fl:
            contents= (fl.read())
        
        cnt = contents.split()
        return len(cnt)
    except:
        pass #ignore and swallow the exception

filenam1 = ('first.py','second.py','third.py')
for f1 in filenam1:
    print(count_words(f1))

