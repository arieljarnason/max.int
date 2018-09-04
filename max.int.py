num_int = int(input("Input a number: "))    # Do not change this line

while 1:
    num_int2 = int(input("Input another number: "))
    numbers.append(num_int2)
    numbers = [num_int, 0]
    if num_int2 < 0:
     break

    max_int = max(numbers)


print("The maximum is", max_int)    # Do not change this line

#Design an algorithm that finds the maximum positive integer input by a user.  
#The user repeatedly inputs numbers until a negative value is entered.
#
