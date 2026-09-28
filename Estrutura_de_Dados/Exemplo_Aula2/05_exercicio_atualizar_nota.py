# Exercício 05 - Atualizando uma nota em uma posição específica
# Atualize a nota de um aluno em uma posição específica e mostre o vetor antes e depois da alteração.

notas = [8.5, 7.0, 9.2, 6.8, 10.0]

print("Notas antes da alteração:", notas)

indice = int(input("Digite o índice da nota que deseja alterar: "))

if 0 <= indice < len(notas):
    nova_nota = float(input("Digite a nova nota: "))
    nota_antiga = notas[indice]
    notas[indice] = nova_nota

    print(f"\nNota alterada no índice {indice}: {nota_antiga} -> {nova_nota}")
    print("Notas depois da alteração:", notas)
else:
    print("Índice inválido. A alteração não foi realizada.")
