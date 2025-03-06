with open("ciag.txt", "r") as file:
    numbers = list(map(int, file.readline().split()))

n = len(numbers)
maks = sum(numbers[:3])
for i in range(n):
    suma = sum(numbers[i:i + 3])
    if maks < suma:
        maks = suma
print(maks)
