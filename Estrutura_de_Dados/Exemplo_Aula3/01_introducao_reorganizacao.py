# Exemplo 01 - Por que uma lista precisa se reorganizar?
# Objetivo: apresentar a turma como uma sequência de elementos identificados por índices.

alunos = ["Ana", "Bruno", "Carla", "Diego"]

print("=== ESTADO INICIAL DA TURMA ===")
for indice, aluno in enumerate(alunos):
    print(f"Índice {indice}: {aluno}")

print(f"\nQuantidade atual de alunos: {len(alunos)}")

print("\nSituações que podem alterar a lista:")
print("- entrada de uma nova matrícula;")
print("- cancelamento de uma matrícula;")
print("- busca por um aluno específico.")
