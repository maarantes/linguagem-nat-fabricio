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

    print(f"\nTexto analisado: \n{texto_exemplo}\n")
    for token in doc:
        print(f"Token: {token.text:15} | Lema: {token.lemma_:15} | POS Tag: {token.pos_}")

    print("\n2. Acesso e Metadados do SUBTLEX-pt-BR ----------")
    
    caminho_arquivo_subtlex = "SUBTLEX-PT-BR.tsv"
    
    try:
        df_subtlex = pd.read_csv(caminho_arquivo_subtlex, sep='\t', usecols=['Word', 'FREQcount'])
        
        frequencias = dict(zip(df_subtlex['Word'], df_subtlex['FREQcount']))
        
        print("\nFrequência das palavras do texto com base nas legendas de filmes (SUBTLEX):\n")
        
        for token in doc:
            if token.pos_ == "PUNCT":
                continue
                
            palavra_busca = token.text.lower()
            freq = frequencias.get(palavra_busca, 0)
            
            if freq > 0:
                print(f"Palavra: {palavra_busca:15} | Frequência: {freq}")
            else:
                print(f"Palavra: {palavra_busca:15} | Frequência: Não encontrado!")
                
    except FileNotFoundError:
        print(f"\nO SUBTLEX-PT-BR não foi encontrado!")

if __name__ == "__main__":
    executar_analise()