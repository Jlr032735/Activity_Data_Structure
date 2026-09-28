# Exercício 02 - Calculando a média da turma
# Leia um vetor de 5 notas e calcule a média da turma.

notas = []

for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("\nNotas informadas:", notas)
print(f"Média da turma: {media:.2f}")
