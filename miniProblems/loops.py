# loop assignments

# counting positive numbers
# sum of  even numbers

# take the full table 
# number = 11

# for num in range(1,number):
#     for digit in range(1,11):
#         print(num,'X',digit,'=' ,num*digit)

# reversing the string
name = "DevRohitDudi"
reversedString = ''
for char in name:
    reversedString = char + reversedString
print(reversedString)

# finding repeated character
given_str = 'anna belle'
for char in given_str:
    if given_str.count(char) == 1:
        print("char is:",char)
        break

# factorial using while loop
limit = 10
result = 1
while(limit>=1):
    result *= limit
    limit -= 1

print("factorial of 10 is:",result)

# valid input number loop
# never use infinite loop hc
askLimit = 15
while askLimit > 0:
    inputNumber = int(input("Enter your valid age: "))
    if 0 <= inputNumber <= 100:
        print("Thanks!")
        break
    else:
        print("Invalid age! please try again.")
        askLimit -= 1


# checking the prime number
primeInput= 29
isPrime = True

if(primeInput>0):
    for num in range(2,primeInput):
        if(primeInput % num) == 0:
            isPrime = False
            break
print("isPrime",isPrime)

# finfing unique values in list
fruitList = ['apple','banana','apple','orange','grapes']
fruitsSet = set()
duplicates = 0
for fruit in fruitList:
    if fruit in fruitsSet:
        print("duplicate!")
        duplicates+=1
        continue
    fruitsSet.add(fruit)
print(fruitsSet)
print("total duplicates:",duplicates)


# 