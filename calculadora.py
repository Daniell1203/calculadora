print("==Calculadora==")
n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))

print(f"1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão")

opcao = input("Digite uma opção:")

if opcao == "1":
    print(f"{n1} + {n2}\nTotal = {n1+n2:.3f}")

elif opcao == "2":
    print(f"{n1} - {n2}\nTotal = {n1-n2:.3f}")

elif opcao == "3":
    print(f"{n1} X {n2}\nTotal = {n1*n2:.3f}")

elif opcao == "4":

    if n2 == 0:
        print("Não existe divisão por zero")

    else:
        print(f"{n1} / {n2}\nTotal = {n1/n2:.3f}")

else:
    print("Opção Invalida")