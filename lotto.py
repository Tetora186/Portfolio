import random

ileliczb = int(input("Ile liczb ma zostać wylosowane? : "))
max = int(input("Maksymalna liczba użyta do losowania: "))

liczby = []
i = 0


while i < ileliczb: #Pętla główna
    liczba = random.randint(1, max) #Losowanie
    if liczby.count(liczba) == 0: #Podliczanie
        liczby.append(liczba) #Tylko unikaty
        i = i + 1 #Licznik

print("Oto liczby:", liczby)