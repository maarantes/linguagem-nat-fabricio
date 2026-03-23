import spacy
import pandas as pd

def executar_analise():

    print("1. Análise Spacy ----------")
    
    try:
        nlp = spacy.load("pt_core_news_sm")
    except OSError:
        print("Erro: Modelo PT_CORE_NEWS_SM não encontrado!")
        return

    texto_exemplo = "Eu gosto muito de estudar processamento de linguagem natural."
    doc = nlp(texto_exemplo)

    print(f"\nTexto analisado:\n{texto_exemplo}\n")
    for token in doc:
        print(f"Token: {token.text:15} | Lema: {token.lemma_:15} | POS Tag: {token.pos_}")

    print("\n2. SUBTLEX-pt-BR ----------")
    
    caminho_arquivo_subtlex = "SUBTLEX-PT-BR.tsv"
    
    try:
        df = pd.read_csv(
            caminho_arquivo_subtlex,
            sep='\t',
            usecols=['Word', 'FREQcount', 'CDcount', 'Spellcheck']
        )
        
        dados = {
            row['Word']: {
                'freq': row['FREQcount'],
                'cd': row['CDcount'],
                'valid': row['Spellcheck']
            }
            for _, row in df.iterrows()
        }

        print("\nAnálise das palavras:\n")
        
        for token in doc:
            if token.pos_ == "PUNCT":
                continue
                
            palavra = token.text.lower()
            info = dados.get(palavra)

            if info:
                print(
                    f"Palavra: {palavra:15} | "
                    f"Freq: {info['freq']:8} | "
                    f"CD: {info['cd']:6} | "
                    f"Spellcheck: {info['valid']}"
                )
            else:
                print(f"Palavra: {palavra:15} | Não encontrada!")

    except FileNotFoundError:
        print("Arquivo SUBTLEX não encontrado!")

if __name__ == "__main__":
    executar_analise()