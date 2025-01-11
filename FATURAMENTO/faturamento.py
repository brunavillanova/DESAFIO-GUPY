import json


def calcular_faturamento(faturamento_diario):
    
    dias_com_faturamento = [faturamento['valor'] for faturamento in faturamento_diario if faturamento['valor'] > 0.0]

    if len(dias_com_faturamento) == 0:
        return "Não há dias com faturamento para calcular."

   
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)

  
    media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

   
    dias_acima_media = sum(1 for faturamento in dias_com_faturamento if faturamento > media_faturamento)

    return menor_faturamento, maior_faturamento, dias_acima_media



def carregar_dados_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados


if __name__ == "__main__":
    
    caminho_arquivo = "FATURAMENTO/dados.json"
    
    try:
        faturamento_diario = carregar_dados_json(caminho_arquivo)
        menor_faturamento, maior_faturamento, dias_acima_media = calcular_faturamento(faturamento_diario)

        print(f"Menor faturamento: R${menor_faturamento:.2f}")
        print(f"Maior faturamento: R${maior_faturamento:.2f}")
        print(f"Número de dias com faturamento superior à média mensal: {dias_acima_media}")
    
    except FileNotFoundError:
        print(f"O arquivo {caminho_arquivo} não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo JSON.")
