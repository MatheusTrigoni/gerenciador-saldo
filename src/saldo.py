from os import system
from time import sleep

if __name__ == "__main__":
    system("cls")
    print("Não execute este arquivo, execute o arquivo main.py!")
    sleep(1.5)
    exit()

def atualizar(saldo: float, alter: list = []):
    system("cls")
    print("Saldo atual: R$", "%.2f" % saldo)

    escolha = input("\nO que deseja fazer hoje?\n1 - Somar ao saldo\n2 - Subtrair do saldo\n3 - Resetar saldo\n0 - Salvar alterações e voltar\n")
    
    if escolha == '1':
        system("cls")
        escolha = input("Confirmar escolha: S/N ")
        if escolha.capitalize() == 'S':
            system("cls")
            try:
                valor = float(input("Valor a ser somado ao saldo: "))
                observacao = input("Observação (deixe em branco caso não queira deixar uma observação): ")
                alter.append((f"Foram somados R$ {'%.2f' % valor} ao saldo", observacao))
                return atualizar(saldo + valor, alter)
            except ValueError:
                system("cls")
                print("Valor inválido!")
                sleep(1)
        system("cls")
        print("Retornando...")
        sleep(1.5)
        return atualizar(saldo, alter)
    elif escolha == '2':
        system("cls")
        escolha = input("Confirmar escolha: S/N ")
        if escolha.capitalize() == 'S':
            system("cls")
            try:
                valor = float(input("Valor a ser subtraído do saldo: "))
                observacao = input(("Observação (deixe em branco caso não queira deixar uma observação): "))
                alter.append((f"Foram subtraídos R$ {'%.2f' % valor} do saldo", observacao))
                return atualizar(saldo - valor, alter)
            except ValueError:
                system("cls")
                print("Valor inválido!")
                sleep(1)
        system("cls")
        print("Retornando...")
        sleep(1.5)
        return atualizar(saldo, alter)
    elif escolha == '3':
        system("cls")
        escolha = input("Confirmar escolha: S/N ")
        if escolha.capitalize() == 'S':
            system("cls")
            alter.append(("O saldo foi resetado", ''))
            return atualizar(0.00)
        system("cls")
        print("Retornando...")
        sleep(1.5)
        return atualizar(saldo, alter)
    elif escolha == '0':
        system("cls")
        print("Retornando...")
        sleep(1.5)
        system("cls")
        return (saldo, alter)
    system("cls")
    print("Opção inválida, retornando...")
    sleep(1.5)
    return atualizar(saldo, alter)