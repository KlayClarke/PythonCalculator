end = False

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
    
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}
while not end:
    
    num1 = int(input('What\'s the first number? '))

    for operation in operations:
        print(operation)

    operation_symbol = input('Please type an operation from the list above: ')
    num2 = int(input('What\'s the next number? '))
    function = operations[operation_symbol]
    answer = function(num1,num2)

    print(f'{num1} {operation_symbol} {num2} = {answer}')

    calc_with_answer = int(input("Type '1' to continue calculating with the answer. Type '2' to end. "))

    if calc_with_answer == 2:
        print('Goodbye! ')
        end = True
    elif calc_with_answer == 1:
        operation_symbol = input('Please type another operation. ')
        print(operation_symbol)
        num3 = int(input('What\'s the next number? '))
        function = operations[operation_symbol]
        second_answer = function(answer, num3)
        print(f'{answer} {operation_symbol} {num3} = {second_answer}')
        again = int(input("Type '1' to calculate again. Type '2' to end. "))
        if again == 2:
            print('Goodbye!')
            end = True
        elif again == 1:
            end = False
        else:
            print('Invalid repsonse.')
            end = True
    
