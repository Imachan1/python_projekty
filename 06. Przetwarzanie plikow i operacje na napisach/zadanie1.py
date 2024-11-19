imie=input("Podaj imie: ")
nazwisko=input("Podaj nazwisko: ")

with open("dane_osobowe.txt","w") as file:
    file.write(imie + "\n")
    file.write(nazwisko)