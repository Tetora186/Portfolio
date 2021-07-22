#Plik na którym przeprowadzone zostaną obliczenia, odczyt
file = open(input("Wprowadź ścieżkę do pliku: "), 'r', encoding='utf=8')


#Liczydło
lines = file.read().splitlines()
#words = open(file('rb')).split()


print("Plik zawiera:", len(lines), " wierszy")

#print(words, " słów")
