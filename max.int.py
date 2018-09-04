num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int

while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int

print("The maximum is", max_int)    # Do not change this line

#Design an algorithm that finds the maximum positive integer input by a user.  
#The user repeatedly inputs numbers until a negative value is entered.
#
