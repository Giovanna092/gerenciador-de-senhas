senha = 1
fila = []

while(True):

    print("-" * 40)
    print("SIMULADOR DE SENHAS")
    print("-" * 40)
    print(" N - Retirar senha")
    print(" C - Chamar senha")
    print("-" * 40)
    
    comando = input("Digite o comando desejado: ")

    # Retirar senha:
    print("-" * 40)
    if comando == "N" or comando == "n":
      
        print (f"Sua senha é: {senha}")
        fila.append(senha)
        print(f"Fila atual: {fila}")
        senha = senha + 1

        qtdSenha = len(fila)
        print(f"Pessoas na fila: {qtdSenha}")


    # Chamar senha:
    print("-" * 40)
    if comando == "C" or comando == "c":


        print(f"Din Dom - senha: {fila[0]}")
        fila.pop(0)
        print(f"Fila atual: {fila}")
        qtdSenha = len(fila)
        print(f"Pessoas na fila: {qtdSenha}")




               
