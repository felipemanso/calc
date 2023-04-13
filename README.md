I'm learning python and I've written a simple calculator in Python that uses addition, subtraction, multiplication and division functions, as well as a simple rule of three.
The user chooses the desired operation and types the numbers to be calculated.
The clear_screen function uses the os module to clear the terminal screen.
The add, subtract, multiply, and divide functions perform the basic math operations of addition, subtraction, multiplication, and division, respectively.
The rule_of_three function calculates the simple rule of three from three numerical values.
The program enters a while True loop that is only interrupted when the user chooses the exit option (6).
Inside the loop, the screen is cleared and a menu with available options is displayed.
The user chooses the desired option by typing a number from 1 to 6.
If the chosen option is 6, the loop is interrupted and the program ends.
If the chosen option is 1, 2, 3 or 4, the user is asked to enter two numbers, which are passed as arguments to the corresponding functions.
If the chosen option is 5, the user is asked to enter three numbers, which are passed as arguments to the rule_of_three function.
If there are any typos or attempts to divide by zero, an error message is displayed and the loop continues.
Finally, the result is displayed on the screen and the user is prompted to press ENTER to continue.
