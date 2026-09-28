# Exemplo 04 - Remoção: fechando o espaço deixado na lista
# Objetivo: remover Carla e deslocar os elementos posteriores para a esquerda.

lista_alunos = ["Ana", "Eduardo", "Bruno", "Carla", "Diego", None]
tamanho = 5
posicao_removida = 3
aluno_removido = lista_alunos[posicao_removida]

print("=== REMOÇÃO EM UMA LISTA SEQUENCIAL ===")
print("Antes :", lista_alunos[:tamanho])
print(f"Remover {aluno_removido} do índice {posicao_removida}\n")

for indice in range(posicao_removida, tamanho - 1):
    aluno_movido = lista_alunos[indice + 1]
    lista_alunos[indice] = aluno_movido
    print(f"Deslocamento: {aluno_movido} | índice {indice + 1} -> {indice}")

lista_alunos[tamanho - 1] = None
tamanho -= 1

print("\nDepois:", lista_alunos[:tamanho])
print("Estrutura completa:", lista_alunos)
