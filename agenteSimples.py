import random

# 0 = limpo  1 = parede  2 = sujo
sala = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

# gerar sujeira aleatoriamente
for linha in range(1, 5):
    for coluna in range(1, 5):

        if random.random() < 0.4:
            sala[linha][coluna] = 2

# Garante que exista pelo menos uma sujeira.
if all(
    sala[linha][coluna] != 2
    for linha in range(1, 5)
    for coluna in range(1, 5)
):
    linhaSujeira = random.randint(1, 4)
    colunaSujeira = random.randint(1, 4)
    sala[linhaSujeira][colunaSujeira] = 2

# posicao inicial do robo aleatoria
posLinha = random.randint(1, 4)
posColuna = random.randint(1, 4)
posicaoInicial = (posLinha, posColuna)

# func mapeamento com um ciclo de 16 movimentos
def funcaoMapear(linha, coluna):
    # Linha 1: esquerda para direita
    if linha == 1 and coluna in (1, 2, 3):
        return "direita"
    elif linha == 1 and coluna == 4:
        return "abaixo"

    # Linha 2: direita para esquerda
    elif linha == 2 and coluna in (4, 3):
        return "esquerda"
    elif linha == 2 and coluna == 2:
        return "abaixo"
    elif linha == 2 and coluna == 1:
        return "acima"

    # Linha 3: esquerda para direita
    elif linha == 3 and coluna == 1:
        return "acima"
    elif linha == 3 and coluna in (2, 3):
        return "direita"
    elif linha == 3 and coluna == 4:
        return "abaixo"

    # Linha 4: direita para esquerda
    elif linha == 4 and coluna in (4, 3, 2):
        return "esquerda"
    elif linha == 4 and coluna == 1:
        return "acima"

# agente reativo simples
def agenteReativoSimples(percepcao):
    linha = percepcao[0]
    coluna = percepcao[1]
    estado = percepcao[2]

    # Se a posição estiver suja, aspira.
    if estado == 2:
        return "aspirar"
    # Se estiver limpa, segue o mapeamento.
    return funcaoMapear(linha, coluna)

# executar a acao - passo a passo
def executarAcao(acao):
    global posLinha, posColuna

    if acao == "aspirar":
        sala[posLinha][posColuna] = 0

    elif acao == "acima":
        if sala[posLinha - 1][posColuna] != 1:
            posLinha -= 1
            
    elif acao == "abaixo":
        if sala[posLinha + 1][posColuna] != 1:
            posLinha += 1

    elif acao == "esquerda":
        if sala[posLinha][posColuna - 1] != 1:
            posColuna -= 1

    elif acao == "direita":
        if sala[posLinha][posColuna + 1] != 1:
            posColuna += 1

# mostrar a sala no console
def mostrarSala():
    print()
    for linha in range(6):
        for coluna in range(6):
            if linha == posLinha and coluna == posColuna:
                print("A", end=" ")
            else:
                print(sala[linha][coluna], end=" ")

        print()
    print()

# execucao do agente
print("Posição inicial da sala:")
mostrarSala()
print("Posição inicial do robô:", posicaoInicial)
passos = 0
movimentos = 0

# O ciclo possui 16 movimentos.
# Cada posição é visitada e, se estiver suja, aspirada.
while movimentos < 16:
    percepcao = [
        posLinha,
        posColuna,
        sala[posLinha][posColuna]
    ]
    acao = agenteReativoSimples(percepcao)

    print("Percepção:", percepcao)
    print("Ação escolhida:", acao)
    executarAcao(acao)
    passos += 1

    # Aspiração não conta como movimento.
    if acao != "aspirar":
        movimentos += 1

    mostrarSala()

# parte final
print("Posição final do robô:", (posLinha, posColuna))

if movimentos <= passos:
    print("Sala está limpa! Ufa")
else:
    print("Ainda existe sujeira na sala.")

print("Total de ações feitas:", passos)
print("Total de movimentos:", movimentos)