print("Witaj w kalkulatorze.\nJakie działanie chcesz przeprowadzić?")

while(True):
    sign = input("+ dodawanie, - odejmowanie, * mnożenie, / dzielenie, ** podnieś do potęgi, x zakończ ")

    if (sign == '+'):
        print(float(input("Wprowadź 1. liczbę: ")) + float(input("Wprowadź 2. liczbę: ")))

    elif (sign == '-'):
        print(float(input("Wprowadź 1. liczbę: ")) - float(input("Wprowadź 2. liczbę: ")))

    elif (sign == '*'):
        print(float(input("Wprowadź 1. liczbę: ")) * float(input("Wprowadź 2. liczbę: ")))

    elif (sign == '/'):
        print(float(input("Wprowadź 1. liczbę: ")) / float(input("Wprowadź 2. liczbę: ")))

    elif (sign == '**'):
        print(float(input("Wprowadź liczbę: ")) ** float(input("Do jakiej potęgi podnieść liczbę: ")))

    elif (sign == 'x'):
        break

    else:
        print("Nierozpoznana funkcja")