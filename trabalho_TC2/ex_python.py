import re

texto = "A reunião de alinhamento está marcada para 15/05/2026. O prazo final do projeto é 20/05/2026, não se atrase!"

padrao_data = r'\b\d{2}/\d{2}/\d{4}\b'

datas_encontradas = re.findall(padrao_data, texto)
print("1. Datas encontradas na string:")
print(datas_encontradas)

primeira_data = re.search(padrao_data, texto)
if primeira_data:
    print("\n2. Primeira data encontrada:")
    print(f"Valor: {primeira_data.group()} (Inicia no índice {primeira_data.start()} e termina no {primeira_data.end()})")

texto_censurado = re.sub(padrao_data, '[DATA OCULTA]', texto)
print("\n3. Texto com as datas substituídas:")
print(texto_censurado)
