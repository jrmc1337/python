n1 = int(input("digite o primeiro numero"))
n2 = int(input("digite o segundo numero"))
n3 = int(input("digite o terceiro numero"))
if n1> n2 and n3:
    print(f'o maior número é: {n1}')
elif n2 > n1 and n2 > n3:
    print(f'o maior número é: {n2}')
else:
    print(f' o maior número é: {n3}')