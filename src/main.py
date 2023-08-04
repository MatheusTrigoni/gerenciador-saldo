import caminho
import saldo
from datetime import date

diretorio = caminho.definir()
linhas = []

try:
    with open(rf"{diretorio}", 'r') as file:
        for i in file:
            linhas.append(i.strip("\n"))
        valor_original = float(linhas[1].strip("R$ "))
except FileNotFoundError:
    valor_original = 0.00

exe = saldo.atualizar(valor_original)

with open(rf"{diretorio}", 'w') as file:
    file.write(f"{(date.today().strftime('%d/%m/%Y'))}\n") # Escreve no arquivo a data de hoje
    file.write(f"R$ {'%.2f' % exe}")