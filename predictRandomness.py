"""
Starts of with input processing.
In order to train the machine to predict the next user input,
the program need to collect data about the user.
In the beginning, the data will be kept in a string of the format of 0s and 1s.
All other symbols is excluded.
"""

list_zero_one = []
symbol_left = 100

while len(list_zero_one) < symbol_left:
    user_input = input("Print a random string containing 0 or 1: ")
    list_zero_one += [x for x in user_input if x == "1" or x == "0"]
    print("Current data length is ", len(list_zero_one), "'", (symbol_left - len(list_zero_one)), "symbols left")
    ## print(listOfZeroAndOne) str list of the user input before converting to int

print(int("".join(list_zero_one)))