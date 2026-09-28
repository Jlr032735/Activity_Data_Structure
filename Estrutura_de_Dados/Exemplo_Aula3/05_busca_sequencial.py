# Exemplo 05 - Busca: encontrando um aluno posição por posição
# Objetivo: localizar Diego por busca sequencial e contar as comparações realizadas.

alunos = ["Ana", "Eduardo", "Bruno", "Carla", "Diego"]
procurado = input("Digite o nome do aluno que deseja procurar: ")

posicao = -1
comparacoes = 0

print("=== BUSCA SEQUENCIAL ===")
print("Lista:", alunos)
print(f"Aluno procurado: {procurado}\n")

for indice, aluno in enumerate(alunos):
    comparacoes += 1
    print(f"Comparação {comparacoes}: índice {indice} -> {aluno}")
    if aluno == procurado:
        posicao = indice
        break

if posicao != -1:
    print(f"\n{procurado} encontrado no índice {posicao}.")
    print(f"Comparações realizadas: {comparacoes}")
else:
    print("\nAluno não encontrado.")
    print(f"Comparações realizadas: {comparacoes}")
