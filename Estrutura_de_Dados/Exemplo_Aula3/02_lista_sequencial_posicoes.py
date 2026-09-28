# Exemplo 02 - Lista sequencial: posições, tamanho e capacidade
# Objetivo: visualizar posições ocupadas e espaços livres em uma representação didática.

capacidade = 6
tamanho = 4
lista_alunos = ["Ana", "Bruno", "Carla", "Diego", None, None]

print("=== REPRESENTAÇÃO SEQUENCIAL DA TURMA ===")
for indice in range(capacidade):
    if indice < tamanho:
        print(f"Índice {indice}: {lista_alunos[indice]}")
    else:
        print(f"Índice {indice}: LIVRE")

print(f"\nTamanho atual : {tamanho}")
print(f"Capacidade    : {capacidade}")
print(f"Espaços livres: {capacidade - tamanho}")


lista_alunos [4] = "José" 