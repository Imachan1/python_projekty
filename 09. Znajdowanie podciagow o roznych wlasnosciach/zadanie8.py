def StringIsNotASC(x):
    for i in range(len(x) - 1):
        if x[i] < x[i + 1]:
            return False
    return True


numbers = list(map(int, input("Podaj ciaj liczb rozdzielonych spacjami: ").split()))
if StringIsNotASC(numbers):
    print("tak")
else:
    print("nie")
