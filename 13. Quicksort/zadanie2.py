def quicksort(ciag):
    n=len(ciag)
    if n<2:
        return ciag
    pivot=ciag[n//2]
    lewy=[x for x in ciag if  x < pivot]
    srodek=[x for x in ciag if  x==pivot]
    prawy=[x for x in ciag if x>pivot]
    return quicksort(lewy)+srodek+quicksort(prawy)

with open("liczby.txt","r") as file:
    c=list(map(int,file.readlines()))

wynik = quicksort(c)
print(wynik)
