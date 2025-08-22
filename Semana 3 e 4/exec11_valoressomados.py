contador = 0
soma = 0


while contador < 10:
    valor = int(input("Adicione um valor {}: ".format(contador)))
    contador = contador+1
    soma = soma+valor

print(soma)