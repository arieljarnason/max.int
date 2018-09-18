n = int(input("Enter the length of the sequence: ")) # Do not change this line

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
for x in range(0, n-3):
    sum = a + b + c
    print(sum)
    a = b
    b = c
    c = sum



#Design an algorithm that generates the first n numbers in the following sequence:
# 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
#Algorithm adds the last three numbers in the row to sum up the new (fourth) number
#Needs to have at least 3 numbers n => 3
#F’(n) = F’(n-1) + F’(n-2) + F’(n-3)