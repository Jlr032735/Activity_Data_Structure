# Exemplo 03 - Inserção: abrindo espaço para um novo aluno
# Objetivo: inserir Eduardo no índice 1 e mostrar os deslocamentos para a direita.

lista_alunos = ["Ana", "Bruno", "Carla", "Diego", None, None]
tamanho = 4
novo_aluno = "Eduardo"
posicao = 3

print("=== INSERÇÃO EM UMA LISTA SEQUENCIAL ===")
print("Antes :", lista_alunos[:tamanho])
print(f"Inserir {novo_aluno} no índice {posicao}\n")

if tamanho == len(lista_alunos):
    print("Não há espaço disponível para a inserção.")
else:
    for indice in range(tamanho, posicao, -1):
        aluno_movido = lista_alunos[indice - 1]
        lista_alunos[indice] = aluno_movido
        print(f"Deslocamento: {aluno_movido} | índice {indice - 1} -> {indice}")

    lista_alunos[posicao] = novo_aluno
    tamanho += 1

    print("\nDepois:", lista_alunos[:tamanho])
    print("Estrutura completa:", lista_alunos)





