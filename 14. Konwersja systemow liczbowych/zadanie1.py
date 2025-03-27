def Binarna():
    binarna=input("")
    czesci = binarna.split(",")
    calkowita=czesci[0]
    ulamek=czesci[1]
    dl_calk = len(calkowita)
    wynik=0
    odwrocona= calkowita[::-1]
    for i in range(dl_calk):
        if odwrocona[i]=="1":
            wynik+=2**(i)
    print(wynik)

Binarna()
