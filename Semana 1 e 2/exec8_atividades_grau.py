grauAP = float(input("Insira sua nota Pratica do Grau A: "))
grauAT = float(input("insira sua nota Teorica do Grau A: "))

grauBPL = float(input("insira sua nota da Prova de Laboratório Grau B: "))
grauBTT = float(input("insita sua nota do Teste Teorico Grau B: "))
grauBTE = float(input("Insira a sua nota do Trabalho de Extraclasse Grau B: "))

grauA_total = ((grauAP*55)+(grauAT*45))/100
grauB_total = ((grauBPL*60)+(grauBTT*20)+(grauBTE*20))/100

print("\nA nota do Grau A: {:.2F}".format(grauA_total))
print("A nota do Grau B: {:.2F}".format(grauB_total))
print("A nota total é: {:.2F}".format(((grauA_total*33)+(grauB_total*67))/100))

#Levando em consideração que é de 0 a 100 os numeros que podem ser aceitos nessa atividade