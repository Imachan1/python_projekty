suma=0
min=100

with open("losowe.txt","r") as file:
    for line in file:
        numbers=int(line.rstrip())
        if min>numbers:
            min=numbers
        suma+=numbers
        
print(suma)
print(min)

            