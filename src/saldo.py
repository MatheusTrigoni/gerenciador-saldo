from os import system
from time import sleep

if __name__ == "__main__":
    system("cls")
    print("Não execute este arquivo, execute o arquivo main.py!")
    sleep(1.5)
    exit()

def atualizar(saldo: float) -> float:
    system("cls")
    print("Saldo atual: R$", "%.2f" % saldo)

    escolha = input("\nO que deseja fazer hoje?\n1 - Somar ao saldo\n2 - Subtrair do saldo\n3 - Resetar saldo\n0 - Salvar alterações e sair\n")
    
    if escolha == '1':
        system("cls")
        escolha = input("Confirmar escolha: S/N ")
        if escolha.capitalize() == 'S':
            system("cls")
            try:
                valor = float(input("Valor a ser somado ao saldo: "))
                return atualizar(saldo + valor)
            except ValueError:
                system("cls")
                print("Valor inválido!")
                sleep(1)
        system("cls")
        print("Retornando...")
        sleep(1.5)
        return atualizar(saldo)
    elif escolha == '2':
        system("cls")
        escolha = input("Confirmar escolha: S/N ")
        if escolha.capitalize() == 'S':
            system("cls")
            try:
                valor = float(input("Valor a ser subtraído do saldo: "))
                return atualizar(saldo - valor)
            except ValueError:
                system("cls")
                print("Valor inválido!")
                sleep(1)
        system("cls")
        print("Retornando...")
        sleep(1.5)
        return atualizar(saldo)
    elif escolha == '3':
        system("cls")
        escolha = input("Confirmar escolha: S/N ")
        if escolha.capitalize() == 'S':
            system("cls")
            return atualizar(0.00)
        system("cls")
        print("Retornando...")
        sleep(1.5)
        return atualizar(saldo)
    elif escolha == '0':
        system("cls")
        print("Volte sempre!")
        sleep(1.5)
        system("cls")
        return saldo
    system("cls")
    print("Opção inválida, retornando...")
    sleep(1.5)
    return atualizar(saldo)