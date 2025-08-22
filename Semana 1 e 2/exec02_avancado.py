A = int(input("Insira o valor A: "))
B = int(input("Insira o valor B: "))
C = int(input("Insira o valor C: "))
x1 = (-B+((B**2-(4*A*C))**(1/2)))/(2*A)
x2 = (-B-((B**2-(4*A*C))**(1/2)))/(2*A)

print("\nO valor de x' é: ",x1)
print("O valor de x'' é: ",x2)