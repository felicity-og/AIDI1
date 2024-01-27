# Python program to check if year is a leap year or not
# use int() to ensure the user input is converted to int for further analysis
print("Is this year a leap year:")
year= int(input())

# the rule of thumb is; if a year is evenly divisible by 400  and its a century year i.e '00s then it is a leap year (366)
# or, if it is evenly divisible by 4 and not by 100 (not a century year) then it is a leap year 
# otherwise it is not
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))