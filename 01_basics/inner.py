# string is immutable, it does'nt accept new changes inside it, we can only pass a
#  new  reference of value at memory into it

username = "devRohitDudi"
newUsername = "new"+username 
# it is passing reference of value at memory that is pointing username, not variable reference

# if the value at memory is pointed to another variable than it will not delete even if the main variable(that created the memory )reference  is changed

print("username is:",username)
print("new username is:",newUsername)

print("first index value of username is: ",username[0])

username = "changed-DevRohitDudi"
print("changed username is:",username)
print("and new username is:",newUsername)

# username[0] = "a"; string is immutable immutable
