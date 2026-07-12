n = int(input("digite um numero: "))

if n <= 1:
    print("Não é primo")
else:
    primo = True

    for i in range(2, n):
        if n % i == 0:
            primo = False
            break

    if primo:
        print("\033[33m É primo")
    else:
        print("\033[31m Não é primo")