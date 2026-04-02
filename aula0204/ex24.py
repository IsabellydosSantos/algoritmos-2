dados = [{"dia": 16, "mes": 1, "ano": 2032, "temp": 30.5},
{"dia": 13, "mes": 2, "ano": 2032, "temp": 29.1},
{"dia": 17, "mes": 3, "ano": 2032, "temp": 28.5},
{"dia": 25, "mes": 4, "ano": 2032, "temp": 26.4}]

for item in dados:
    dia = item["dia"]
    mes = item["mes"]
    ano = item["ano"]
    temp = item["temp"]

    print(f"{dia}/{mes:02d}/{ano}: Temperatura: {temp}°C")