
# #Enter price (dollars, numerator, denominator): 29 7 8
# 100 shares with market price 29 7/8 have value $2987.50
    
def user_input():
    """Accepts user input and sends out for calculations"""
    shares_error_msg = " Invalid number!"
    price_error_msg = " Invalid price!"

    while 1: #loopar þar til þú skrifar inn int
        try:
            shares_entered = int(input("Enter number of shares: "))
            break
        except ValueError:
            print(shares_error_msg)
    
    while 1: #loopar þar til þú skrifar inn 3 x integers
        try:
            dollars_entered, numerator_entered, denominator_entered = map(int, input("Enter price (dollars, numerator, denominator):").split())
            break
        except ValueError:
            print(price_error_msg)

    return shares_entered, dollars_entered, numerator_entered, denominator_entered

def printer(msg1, msg2, msg3, msg4, msg5):
    """Prints out messages msg1, msg2, msg3,msg4, msg5"""
    print(' ',msg1,"shares with market price",msg2, "{}/{} have value ${}".format(msg3, msg4, format(msg5, ".2f")))

def continue_program():
    yes_or_no = input("Continue: ")
    if "y" in yes_or_no:
        stop_program = False; return stop_program
    elif "n" in yes_or_no:
        stop_program = True; return stop_program


def calculator(shares, dollars, numerator, denominator):
    dollars += numerator / denominator
    value = float(dollars * shares)

    return shares, dollars, numerator, denominator, value

while 1:

    int1, int2, int3, int4 = user_input()
    int1_calc, int2_calc, int3_calc, int4_calc, value_calc = calculator(int1, int2, int3, int4)
    printer(int1, int2, int3, int4, value_calc)

    stop = continue_program()
    if stop == True: break

    
