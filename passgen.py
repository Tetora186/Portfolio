import random

how_many_char = int(input("Ile znaków ma mieć hasło?: "))

sign = range(33, 127)
passc = ("")

#Pobieranie znaków z ASCII

for i in range(how_many_char):
    passc += chr(random.choice(sign))

print("Wygenerowane hasło to: ", passc)