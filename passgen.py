from random import choice

print("Witaj w generatorze haseł.")

sign = range(33, 127)
passgen = ()

# Wprowadzam liczbę znaków do wygenerowania i zamieniam to w liczbę

cnt_sign = input("Iluznakowe hasło chcesz wygenerować?: ")

# Pętla która ma wylosować ilość znaków wpisaną w poprzednim kroku

for i in cnt_sign:
    passgen += chr(choice(sign))


print("Gotowe hasło to:")
print(passgen)
