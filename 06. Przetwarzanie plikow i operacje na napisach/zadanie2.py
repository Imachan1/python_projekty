with open("dane_osobowe.txt","r") as file:
    content=file.read().rstrip()
    
print(f"Witaj \n {content}")