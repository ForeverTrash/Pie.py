"""
#Creates a list with three options
fruits = ["boy", "girl", "other"]
#Assigns variables to each item on the list (unpack)
x, y, z = fruits
print(x, y, z)
w = input("What other sexuality is there?: ")
fruits.append(w)
print(fruits)
"""
import sys

while True:

    # Math
    pi = 3.14159
    # File reading
    help_text = open("files/help_text.txt","r")
    # Command lists
    help_command_list = ["HELP", "Help", "/H", "/h", "/Help", "/help"]
    pi_squared_command_list = ["Pi", "pi", "/Pi", "/pi", "pi squared", "Pi squared"]
    quit_command_list = ["quit()", "Quit()", "quit", "Quit", "/Quit", "/quit"]
    
    # Pi-Squared Function
    def pi_squared(x):
        # Set value of variable user_request to input taken for math function
        user_request = x
        # Create variable calculate which calcs pi squared ( To the 2nd power )
        calculate = pi ** int(user_request)
        print("Pi squared to the ", user_request, " power = ", calculate)

    # Ask user which program they'd like to use 
    user_input = input("What progam would you like to use? (Type HELP for help): ")

    # Help Program
    if user_input in help_command_list:
        # Create and print variable to read the file defined in help_text
        help_text_content = help_text.read()
        print(help_text_content)

    # Pi-Squared Program
    if user_input in pi_squared_command_list:
        user_request = input("What power would you like to square pi to? ( Max of 600 ): ")
        # Run pi-squared math function
        pi_squared(user_request)
        
    # Quit Program
    if user_input in quit_command_list:
        print("Closing program")
        sys.exit()
        
    # After command waits for input to start at the beginning of the script
    continue_script = input("Press ENTER to continue")
    continue
"""
TODO:

Exponent math both variables choosable by user
"""

