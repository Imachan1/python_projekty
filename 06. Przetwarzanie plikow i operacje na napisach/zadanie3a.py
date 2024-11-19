import random

    
with open("losowe.txt","w") as file:
    for i in range(100):
        numbers=random.randint(1,10)
        file.write(f"{numbers}\n")