def converta(data: str) -> str:
    data_lista = list(data)
    return f"{''.join(data_lista[8:])}/{''.join(data_lista[5:7])}/{''.join(data_lista[0:4])}"