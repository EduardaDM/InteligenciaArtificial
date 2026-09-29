"""
0 = limpo | 1 = parede | 2 = sujo
O agente começa em (1, 1), percorre a sala em zigue-zague e para com NoOp.
"""
import random

sala = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
]

for l in range(1, 5):
    for c in range(1, 5):
        if random.random() < 0.4:
            sala[l][c] = 2

posLinha = 1
posColuna = 1
pontos = 0


def funcaoMapear(linha, coluna):
    # Caminho serpentino que cobre todas as casas da sala 4x4
    if linha == 1:
        return "direita" if coluna < 4 else "abaixo"
    if linha == 2:
        return "esquerda" if coluna > 1 else "abaixo"
    if linha == 3:
        return "direita" if coluna < 4 else "abaixo"
    if linha == 4:
        return "esquerda" if coluna > 1 else "NoOp"


def checkObj(sala):
    for l in range(1, 5):
        for c in range(1, 5):
            if sala[l][c] == 2:
                return 1
    return 0


def agenteObjetivo(percepcao, objObtido):
    linha, coluna, estado = percepcao
    if objObtido == 0:
        return "NoOp"
    if estado == 2:
        return "aspirar"
    return funcaoMapear(linha, coluna)


def executarAcao(acao):
    global posLinha, posColuna
    if acao == "aspirar":
        sala[posLinha][posColuna] = 0
    elif acao == "acima" and sala[posLinha - 1][posColuna] != 1:
        posLinha -= 1
    elif acao == "abaixo" and sala[posLinha + 1][posColuna] != 1:
        posLinha += 1
    elif acao == "esquerda" and sala[posLinha][posColuna - 1] != 1:
        posColuna -= 1
    elif acao == "direita" and sala[posLinha][posColuna + 1] != 1:
        posColuna += 1


def mostrarSala():
    for l in range(6):
        linha = []
        for c in range(6):
            linha.append("A" if (l, c) == (posLinha, posColuna) else str(sala[l][c]))
        print(" ".join(linha))
    print()


if __name__ == "__main__":
    print("Estado inicial:")
    mostrarSala()
    while True:
        percepcao = [posLinha, posColuna, sala[posLinha][posColuna]]
        objObtido = checkObj(sala)
        acao = agenteObjetivo(percepcao, objObtido)
        print(f"Percepção: {percepcao} | Objetivo obtido: {objObtido} | Ação: {acao}")
        if acao == "NoOp":
            break
        executarAcao(acao)
        pontos += 1  # Conta movimentos e aspirações executadas
        mostrarSala()
    print("Objetivo atingido: sala sem sujeira.")
    print("Quantidade de passos (pontos):", pontos)