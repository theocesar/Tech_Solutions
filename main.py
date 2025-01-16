def questao_indice():
    indice = 13
    soma = 0
    k = 0

    while k < indice:
        k += 1
        soma += k

    print(f"O valor da variável SOMA é: {soma}")


def questao_fibonacci():

    def pertence_fibonacci(n):
        a, b = 0, 1

        while a < n:
            a, b = b, a + b

        return a == n

    numero = int(input("(Questão 2) Informe um número: "))
    if pertence_fibonacci(numero):
        print(f"(Questão 2) O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"(Questão 2) O número {numero} não pertence à sequência de Fibonacci.")


def questao_json():
    # a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; NÃO ENCONTREI ESSE JSON, POR ISSO CRIEI DADOS SINTÉTICOS
    import json

    # Dados sintéticos
    dados_faturamento = """
    {
        "faturamento_diario": [100, 200, 0, 300, 0, 0, 500, 600, 0, 400, 0, 0, 700, 0, 800]
    }
    """
    dados = json.loads(dados_faturamento)["faturamento_diario"]

    # Obter só os dias com faturamento
    dias_validos = [f for f in dados if f > 0]

    menor_faturamento = min(dias_validos)
    maior_faturamento = max(dias_validos)
    media_mensal = sum(dias_validos) / len(dias_validos)
    dias_acima_da_media = sum(1 for f in dias_validos if f > media_mensal)

    print(f"(Questão 3) Menor faturamento: {menor_faturamento}")
    print(f"(Questão 3) Maior faturamento: {maior_faturamento}")
    print(f"(Questão 3) Dias com faturamento acima da média: {dias_acima_da_media}")


def questao_faturamento():

    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    total = sum(faturamento_estados.values())

    print("(Questão 4) Percentual de representação por estado:")
    for estado, valor in faturamento_estados.items():
        percentual = (valor / total) * 100
        print(f"{estado}: {percentual:.2f}%")


def questao_inversao():

    def inverte_string(string):
        return string[::-1]

    entrada = input("(Questão 5) Informe uma string: ")
    print(f"(Questão 5) String invertida: {inverte_string(entrada)}")


if __name__ == "__main__":
    questao = int(input("Qual questão gostaria de executar? 1,2,3,4 ou 5?"))

    match questao:
        case 1:
            questao_indice()
        case 2:
            questao_fibonacci()
        case 3:
            questao_json()
        case 4:
            questao_faturamento()
        case 5:
            questao_inversao()
        case _:
            print("Opção inválida! Escolha as opçoes válidas: 1, 2, 3, 4 ou 5.")


