# Exemplo 06 - Deslocamento: o movimento escondido nas alterações
# Objetivo: comparar o deslocamento para a direita e para a esquerda.

print("=== DESLOCAMENTO PARA A DIREITA ===")
direita = ["Ana", "Bruno", "Carla", "Diego", None]
tamanho = 4
posicao_insercao = 2

print("Antes :", direita[:tamanho])
print("Inserção de Eduardo no índice 2")

for indice in range(tamanho, posicao_insercao, -1):
    aluno = direita[indice - 1]
    direita[indice] = aluno
    print(f"{aluno}: índice {indice - 1} -> {indice}")

direita[posicao_insercao] = "Eduardo"
tamanho += 1
print("Depois:", direita[:tamanho])

print("\n=== DESLOCAMENTO PARA A ESQUERDA ===")
esquerda = ["Ana", "Bruno", "Carla", "Diego", None]
tamanho = 4
posicao_remocao = 1

print("Antes :", esquerda[:tamanho])
print("Remoção de Bruno do índice 1")

for indice in range(posicao_remocao, tamanho - 1):
    aluno = esquerda[indice + 1]
    esquerda[indice] = aluno
    print(f"{aluno}: índice {indice + 1} -> {indice}")

esquerda[tamanho - 1] = None
tamanho -= 1
print("Depois:", esquerda[:tamanho])
