import math

a= float(input('Digite o angulo em graus: '))
rad= math.radians(a)

sen= math.sin(rad)
cos= math.cos(rad)
tan= math.tan(rad)

print(f"Seu angulo seno vale {sen:.2f} ")
print(f"Seu angulo cosseno vale {cos:.2f}")
print(f"Seu angulo tangente vale {tan:.2f}")
