import caminho
import saldo
from datetime import date

while True:
    diretorio = caminho.definir()

    with open(rf"{diretorio}", 'r') as file:
        linhas = file.readlines()

        if len(linhas) > 0:
            valor_original = float(linhas[-2].lstrip("SALDO ATUAL -> R$ "))
        else:
            valor_original = 0.00

    exe = saldo.atualizar(valor_original)

    with open(rf"{diretorio}", 'a') as file:
        file.write(f"{(date.today().strftime('%d/%m/%Y'))}\n") # Escreve no arquivo a data de hoje
        for alteracoes in exe[1]:
            file.write(f"ALTER -> {alteracoes[0]}\n")
            if alteracoes[1] != '':
                file.write(f"OBS -> {alteracoes[1]}\n")
        file.write(f"SALDO ATUAL -> R$ {'%.2f' % exe[0]}\n")
        file.write("==============================================\n")