def addition(a, b):
	return(a + b)

def subtraction(a, b):
	return(a - b)

def multiplication(a, b):
	return(a * b)

def division(a, b):
	return(a / b)

def calc_parser(calc_string):
    calc_list = calc_string.split(' ')
    calc_list[0] = float(calc_list[0])
    calc_list[2] = float(calc_list[2])
    return calc_list

calculator_func_dict = {'-': subtraction,
                        '*': multiplication,
			'+': addition,
			'/': division}

calc_string = input('Enter your expression: ')

while calc_string != 'exit':
    command = calc_parser(calc_string)[1]
    if command in calculator_func_dict:
        print(calculator_func_dict[command](calc_parser(calc_string)[0], calc_parser(calc_string)[2]))
    else:
        print('Seems like an invalid expression. Please, enter valid expression!')

    calc_string = input('Enter your expression: ')

print('See you next time!')
