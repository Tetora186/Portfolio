print("Witaj w moim kalkulatorze.\nJakie działanie będziesz chciał przeprowadzać?")

while(True):
    znak = input("+ dodawanie, - odejmowanie, * mnożenie, / dzielenie, ** podnieś do potęgi, x zakończ ")

    if (znak == '+'):
        print(float(input("Wprowadź 1. liczbę: ")) + float(input("Wprowadź 2. liczbę: ")))

    elif (znak == '-'):
        print(float(input("Wprowadź 1. liczbę: ")) - float(input("Wprowadź 2. liczbę: ")))

    elif (znak == '*'):
        print(float(input("Wprowadź 1. liczbę: ")) * float(input("Wprowadź 2. liczbę: ")))

    elif (znak == '/'):
        print(float(input("Wprowadź 1. liczbę: ")) / float(input("Wprowadź 2. liczbę: ")))

    elif (znak == '**'):
        print(float(input("Wprowadź liczbę: ")) ** float(input("Do jakiej potęgi podnieść liczbę: ")))

    elif (znak == 'x'):
        break

    else:
        print("Nierozpoznana funkcja")