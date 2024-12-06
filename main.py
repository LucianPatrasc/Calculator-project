logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide,
}

def calculator():
    print(logo)
    should_accumulate=True
    num1= float(input("Care este primul numar? :"))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("Alege o operatie matematica: ")
        num2= float(input("Care este urmatorul numar? :"))
        answer= operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice= input(f"Scrie 'd' sa continui calculele cu {answer} sau scrie 'n' pentru calcul nou.")
        if choice == "d":
            num1=answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()


