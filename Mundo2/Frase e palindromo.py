f=input("digite a frase:").strip().upper()

r=(f).replace(" ","")

ft= f[::-1].replace(" ","")

print(f'A frase digitada é {ft}')
if r==ft:
    print("palindromo")
else:
    print(f"frase nao palindromo")
