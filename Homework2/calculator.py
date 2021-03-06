"""
Calculate the number with the operator
Parameter
number1: int
	First number to calculate
number2: int
	second number to calculate
operator: str
	the operation
Return
	The number after calculate with the operation
"""
def calculator(number1, number2, operator):
    if operator == '*':
        return number1 * number2
    elif operator == '+':
        return number1 + number2
    elif operator == '**':
        return float(number1 ** number2)
    elif operator == '/':
        return number1 / number2
    elif operator == '-':
        return number1 - number2
    else:
        return 'invalid operator'

"""
Take the input to calculator and print out the input
"""
def input_output():
    while True:
        try:
            number1 = float(input('Enter the first number: '))
            number2 = float(input('Enter the second number: '))
            operator = input('Enter the operation: ')
            print(calculator(number1, number2, operator))
            while True:
            	calc_again= input('Do you wish to continue?(y/n)')
            	if calc_again =='y':
                	print(input_output())
            	elif calc_again == 'n':
                	print('exit')
                	quit()
            	else:
                	print('invalid input')
        except ValueError:
        	print('invalid input')
       

input_output()
