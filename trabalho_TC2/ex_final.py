import re

def executar_exemplos():
    print("--- Exemplo 1: Tokenização por Sentenças ---")
    texto_bruto = "Hoje de manhã Pedro acordou com muita fome. Levantou, escovou os dentes! O que ele fez depois? Abriu a geladeira."
    sentencas = re.split(r'(?<=[.!?]) +', texto_bruto)
    print("Sentenças encontradas:", sentencas)

    print("\n--- Exemplo 2: Extração de Texto de Interesse (E-mails) ---")
    texto_emails = "Para mais informações, contate o suporte no email suporte@empresa.com.br ou fale com joao.silva@teste.com"
    emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', texto_emails)
    print("E-mails extraídos:", emails)

    print("\n--- Exemplo 3: Captura de Texto entre Tags HTML ---")
    texto_html = "<body><p>The product is good!</p><div>Ignorar este bloco</div><p>Thanks folks!</p></body>"
    paragrafos = re.findall(r'<p>(.*?)</p>', texto_html)
    print("Conteúdo dos parágrafos extraídos:", paragrafos)

    print("\n--- Exemplo 4: Extração de Números (Usando novo metacaractere \\d) ---")
    texto_financeiro = "A ação fechou cotada a 25 reais, um aumento de 5 por cento em 2025."
    numeros = re.findall(r'\b\d+\b', texto_financeiro)
    print("Números encontrados:", numeros)

    print("\n--- Exemplo 5: Limpeza e Normalização de Espaços (Usando novo metacaractere \\s) ---")
    texto_sujo = "Este   texto possui\nmuitos     espaços\t e precisa ser normalizado."
    texto_normalizado = re.sub(r'\s+', ' ', texto_sujo)
    print("Texto normalizado:", texto_normalizado)

if __name__ == "__main__":
    executar_exemplos()