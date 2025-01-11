import json

def calcular_faturamento(dados):

    faturamentos = [dia["faturamento"] for dia in dados if dia["faturamento"] > 0]


    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)


    media_mensal = sum(faturamentos) / len(faturamentos)

    dias_acima_da_media = sum(1 for dia in faturamentos if dia > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

with open("FATURAMENTO/dados.json", "r") as arquivo:
    dados = json.load(arquivo)

menor, maior, dias_acima = calcular_faturamento(dados)


print(f"Menor faturamento: R$ {menor:.2f}")
print(f"Maior faturamento: R$ {maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima}")
