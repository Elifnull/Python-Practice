from art import logo
print(logo)

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operation_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator(): #declared function so as to invoke recursion
    num1 = float(input("what is the first number?\n")) #converted int to float for wider range of inputs
    
    end_state = False
    while not end_state:
        
        print("Choose operation to perform:")
        for key in operation_dictionary:
        print(key)
        
        operation = input("which operation do you want to perform? \n")
        
        function = operation_dictionary[operation]
        
        num2 = float(input("what is the next number?\n")) 
        answer = function(num1,num2)
        
        print(f"{num1} {operation} {num2} = {answer}")
        end_calculator = input(f"do you want to continue operations with {answer}, or type 'start' to start new calculation? Write 'Yes', 'No' or 'Start'\n").lower()
        if end_calculator == "no":
        end_state = True
        print("Congratulations, you are done")
        elif end_calculator == "start":
        calculator() #recursion event triggered by "start" condition
        else:
        num1 = answer

calculator()