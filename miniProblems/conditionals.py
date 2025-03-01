# 1: very common
# 2: only nested conditional
# 3: nothing
# 4: nothing



# 9:leap year
year = 2025

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0 ):
    print(year,"is a leap year.")

else:
     print(year,"isn't a leap year.")


# 10:   