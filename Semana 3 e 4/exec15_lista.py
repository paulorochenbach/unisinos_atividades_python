nLista = int(input("Numero de itens da Lista: "))

minhaLista = []
for i in range(0,nLista):
    produto = input("Item a ser adicionado a lista: ")
    minhaLista.append(produto)

print()
print(minhaLista)