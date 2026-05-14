print("   CALCULADORA:   ")

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

print("1 - Soma")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")

opcao = input("Escolha uma opcao: ")

if opcao == "1":
    print(f"Resultado: {n1 + n2}")

elif opcao == "2":
    print(f"Resultado: {n1 - n2}")

elif opcao == "3":
    print(f"Resultado: {n1 * n2}")

elif opcao == "4":
    print(f"Resultado: {n1 / n2}")

else:
    print("Opcao invalida")