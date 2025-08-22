NotaA = int(input("Insira a Nota A: "))
NotaB = int(input("Insira a Nota B: "))

medianotas = ((NotaA*30)+(NotaB*70))/100

if NotaA < 0 or NotaB < 0:
    print("Erro, o sistema náo aceita valores negativos.")
elif medianotas <= 70:
    print("Voce vai ter que realizar a prova de Grau C.")
else:
    print("Voce náo precisa de nota adicionar do Grau C.")
