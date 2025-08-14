n1 = float(input("digite a primeira nota"))
n2 = float(input("digite a segunda nota"))
m = (n1+n2)/2
if m >= 10:
    print(f' A sua Média é {m}, aluno aprovado com distinção')
elif m >= 7:
    print(f' A sua Média é {m}, aluno aprovado')
else:
    print(f' A sua Média é {m}, aluno reprovado')