A = int(input("Insira o Valor de A: "))
B = int(input("Insira o valor de B: "))

if B == 0:
    print("Erro, o valor de B não pode ser 0.")

else:
    print("A divisão de {} por {} é {}".format(A, B, A/B))