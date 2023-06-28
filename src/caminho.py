from os import system, path
from time import sleep
import locale, ctypes

def defina() -> str:
    system("cls")
    print("Olá! Seu arquivo será salvo num bloco de notas.\n")

    user = input("Digite o seu nome de usuário do Windows: ")
    nome_arquivo = input("Digite o nome do arquivo: ")
    escolha = input("Digite onde deseja salvar seu documento:\n1 - Área de Trabalho\n2 - Documentos\n3 - Diretório Personalizado\n0 - Sair\n")
    idioma_id = locale.windows_locale[ ctypes.windll.kernel32.GetUserDefaultUILanguage() ] # Retorna a string que identifica o idioma do sistema

    if escolha == '1' and idioma_id == "en_US":
        if path.exists(f"C:/Users/{user}/Desktop"):
            return f"C:/Users/{user}/Desktop/{nome_arquivo}.txt"
        system("cls")
        print("O diretório não existe.\nRetornando...")
        sleep(1.5)
        return defina()
    elif escolha == '1' and idioma_id == "pt_BR":
        if path.exists(f"C:/Users/{user}/Área de Trabalho"):
            return f"C:/Users/{user}/Área de Trabalho/{nome_arquivo}.txt"
        system("cls")
        print("O diretório não existe.\nRetornando...")
        sleep(1.5)
        return defina()
    elif escolha == '2' and idioma_id == "en_US":
        if path.exists(f"C:/Users/{user}/Documents"):
            return f"C:/Users/{user}/Documents/{nome_arquivo}.txt"
        system("cls")
        print("O diretório não existe.\nRetornando...")
        sleep(1.5)
        return defina()
    elif escolha == '2' and idioma_id == "pt_BR":
        if path.exists(f"C:/Users/{user}/Documentos"):
            return f"C:/Users/{user}/Documentos/{nome_arquivo}.txt"
        system("cls")
        print("O diretório não existe.\nRetornando...")
        sleep(1.5)
        return defina()
    elif escolha == '3':
        system("cls")
        diretorio = input("Digite o diretório completo (não inclua o arquivo): ")
        if path.exists(diretorio):
            return f"{diretorio}/{nome_arquivo}.txt"
        system("cls")
        print("O diretório não existe.\nRetornando...")
        sleep(1.5)
        return defina()
    elif escolha == '0':
        system("cls")
        print("Volte sempre!")
        sleep(1.5)
        system("cls")
        exit()
    
    print("Opção inválida, tente novamente ou digite 0 para sair.\nRetornando...")
    sleep(2)
    return defina()