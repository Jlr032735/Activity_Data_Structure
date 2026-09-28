# Exemplo 07 - Capacidade e custo: a posição altera o trabalho
# Objetivo: comparar deslocamentos em inserções perto do início e no final.

alunos = [
    "Ana", "Bruno", "Carla", "Diego", "Eduardo",
    "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"
]

capacidade = 12
tamanho = len(alunos)

posicao_inicio = 1
posicao_final = tamanho

deslocamentos_inicio = tamanho - posicao_inicio
deslocamentos_final = tamanho - posicao_final

print("=== CAPACIDADE E CUSTO DAS OPERAÇÕES ===")
print(f"Tamanho atual : {tamanho}")
print(f"Capacidade    : {capacidade}")
print(f"Espaços livres: {capacidade - tamanho}\n")

print("Comparação de inserções:")
print(f"- Inserção no índice {posicao_inicio}: {deslocamentos_inicio} deslocamentos")
print(f"- Inserção no final (índice {posicao_final}): {deslocamentos_final} deslocamentos")

print("\nLeitura do custo:")
print("- Acesso por índice: O(1)")
print("- Busca sequencial: O(n)")
print("- Inserção no meio/início: O(n)")
print("- Remoção no meio/início: O(n)")
print("- Percurso completo: O(n)")

if deslocamentos_inicio > deslocamentos_final:
    print("\nConclusão: inserir perto do início exige mais movimentações.")
