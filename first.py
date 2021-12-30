#python is based on indentation

print("Hello kishore")

message = "Hello Python world!"
print(message)

first_name = "ada"
last_name = "lovelace"
#to replace the value of variable in string use f(format) before the quotes
full_name = f"{first_name} {last_name}"
print(full_name)

#title does camel case
message = f"Hello {full_name.title()} \n welcome"
print(message)
print("Languages:\n\tPython\n\tC\n\tJavaScript")


messagewithspace='           pt    '
mes = messagewithspace.strip()#we can also strip only spaces on left and right with rstrip lstrip
print(mes)


#Python doesnt support built-in constant types so use all caps to denote constatnt
MAX_CONNECTIONS = 5000
