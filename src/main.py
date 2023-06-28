from caminho import defina
from saldo import atualize
from datetime import date
from data import converta

diretorio = defina()
linhas = []

try:
    with open(rf"{diretorio}", 'r') as file:
        for i in file:
            linhas.append(i.strip("\n"))
        valor_original = float(linhas[1].strip("R$ "))
except FileNotFoundError:
    valor_original = 0.00

exe = atualize(valor_original)

with open(rf"{diretorio}", 'w') as file:
    file.write(f"{converta(date.isoformat(date.today()))}\n") # Escreve no arquivo a data de hoje
    file.write(f"R$ {'%.2f' % exe}")