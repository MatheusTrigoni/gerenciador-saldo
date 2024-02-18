from os import system, path
from time import sleep
# import locale, ctypes

if __name__ == "__main__":
    system("cls")
    print("Não execute este arquivo, execute o arquivo main.py!")
    sleep(1.5)
    exit()

def definir() -> str:
    system("cls")
    print("Olá! Seus caminhos serão salvos num bloco de notas chamado paths.txt e seus arquivos serão salvos em arquivos .txt de sua escolha.")

    # user = input("Digite o seu nome de usuário do Windows: ")
    # nome_arquivo = input("Digite o nome do arquivo: ")
    # escolha = input("Digite onde deseja salvar seu documento:\n1 - Área de Trabalho\n2 - Documentos\n3 - Diretório Personalizado\n0 - Sair\n")
    if not path.exists("paths.txt"):
        paths = open("paths.txt", 'x')
        paths.close()

    escolha = input("\n1 - Selecionar caminho\n2 - Salvar novo caminho\n3 - Remover caminho\n0 - Sair\n")
    # idioma_id = locale.windows_locale[ ctypes.windll.kernel32.GetUserDefaultUILanguage() ] # Retorna a string que identifica o idioma do sistema

    system("cls")

    if escolha == '1':
        linhas = [linha for linha in open("paths.txt") if linha != "\n"]

        if len(linhas) == 0:
            print("Nenhum caminho presente. Retornando...")
            sleep(1.5)
            return definir()

        mensagem = ''
        for caminho in linhas:
            mensagem += f"{linhas.index(caminho) + 1} - {caminho}\n" # Salvando toda a string em uma variável para não repetir o loop múltiplas vezes
        mensagem += "0 - Voltar\n"

        while True:
            system("cls")
            print(mensagem)

            try:
                escolha = int(input("Selecione o caminho que deseja carregar: "))

                if escolha == 0:
                    system("cls")
                    print("Retornando...")
                    sleep(1.5)
                    return definir()
                else:
                    idx = linhas[escolha - 1]
                    return idx.strip("\n")
            except ValueError:
                system("cls")
                print("ValueError: um valor não númerico foi inserido. Digite 0 para retornar ao menu.")
                sleep(2)
            except IndexError:
                system("cls")
                print("IndexError: o valor inserido não corresponde a um caminho na lista. Digite 0 para retornar ao menu.")
                sleep(2)
    elif escolha == '2':
        caminho = input("Digite o caminho o qual deseja salvar (não inclua o nome do arquivo e a extensão .txt): ")

        if path.exists(caminho):
            while True:
                system("cls")
                print("Digite 0 para cancelar e retornar ao menu.\n")
                try:
                    nome_arquivo = input("Digite o nome do arquivo (inclua a extensão .txt): ")

                    if nome_arquivo == '0':
                        system("cls")
                        print("Retornando...")
                        sleep(1.5)
                        return definir()
                    elif nome_arquivo[-4:] == ".txt":
                        break # Com o nome do arquivo dentro dos conformes, o loop é quebrado, continuando a partir da abertura do arquivo paths.txt
                    else:
                        system("cls")
                        print("Lembre-se de incluir a extensão .txt! Digite 0 para cancelar e retornar ao menu.")
                        sleep(2)
                except IndexError:
                    system("cls")
                    print("IndexError: o tamanho do nome do arquivo é menor do que o esperado. Digite 0 para cancelar e retornar ao menu.")
                    sleep(2)

            linhas = [linha.rstrip("\n") for linha in open("paths.txt") if linha != "\n"]

            caminho_full = caminho + '/' + nome_arquivo
            for linha in linhas:
                if linha == caminho_full:
                    system("cls")
                    print("Um caminho com este nome já foi salvo.\n\nRetornando...")
                    sleep(2)
                    return definir()
                
            novo_arquivo = open(caminho_full, 'x') # Criando o arquivo no determinado diretório
            novo_arquivo.close()
            
            with open("paths.txt", 'a') as paths:
                paths.write(f"{caminho_full}\n\n")
            
            system("cls")
            print("Salvamento concluído. Retornando...")
            sleep(1.5)
            return definir()
        system("cls")
        print(f"O caminho \"{caminho}\" não existe. Retornando...")
        sleep(2)
        return definir()
    elif escolha == '3':
        linhas = [linha for linha in open("paths.txt") if linha != "\n"]

        if len(linhas) == 0:
            print("Nenhum caminho presente. Retornando...")
            sleep(1.5)
            return definir()
        
        while True:
            system("cls")

            for caminho in linhas:
                print(f"{linhas.index(caminho) + 1} - {caminho}")
            print("0 - Voltar\n")

            try:
                escolha = int(input("Selecione o caminho que deseja remover: "))

                if escolha == 0:
                    system("cls")
                    print("Retornando...")
                    sleep(1.5)
                    return definir()
                else:
                    linhas.pop(escolha - 1)
                    sleep(0.5)
                    with open("paths.txt", 'w') as paths:
                        for linha in linhas:
                            paths.write(f"{linha}\n")
            except ValueError:
                system("cls")
                print("ValueError: um valor não númerico foi inserido. Digite 0 para retornar ao menu.")
                sleep(1.5)
            except IndexError:
                system("cls")
                print("IndexError: o valor inserido não corresponde a um caminho na lista. Digite 0 para retornar ao menu.")
                sleep(1.5)
    elif escolha == '0':
        system("cls")
        print("Volte sempre!")
        sleep(1.5)
        system("cls")
        return exit()
    
    print("Opção inválida, tente novamente ou digite 0 para sair.\nRetornando...")
    sleep(1.5)
    return definir()