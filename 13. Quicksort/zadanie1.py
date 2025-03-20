def quicksort(ciag,lewy,prawy):
    i=lewy
    j=prawy
    pivot = ciag[(i+j)//2]
    while i<=j:
        while ciag[i]<pivot:
            i+=1
        while ciag[j]>pivot:
            j-=1
        if i<=j:
            pom=ciag[i]
            ciag[i]=ciag[j]
            ciag[j]=pom
            i+=1
            j-=1
    if j>lewy:
        quicksort(ciag,lewy,j)
    if i<prawy:
        quicksort(ciag,i,prawy)

with open("liczby.txt","r") as file:
    c=list(map(int,file.readlines()))

quicksort(c,0,len(c)-1)
print(c)
