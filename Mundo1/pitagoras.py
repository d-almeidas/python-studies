import math

t= float(input('Digite o valor do cateto oposto : '))
t2= float(input('Digite o valor do cateto adjacente : '))
h= (t**2+t2**2)
h2=math.sqrt(h)
h3= math.ceil(h2)
print(f"A hipotenusa desse triangulo e igual a :{h2:.2f} ou aproximadamente {h3}")


