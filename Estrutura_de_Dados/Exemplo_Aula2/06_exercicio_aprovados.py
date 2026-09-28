# Exercício 06 - Contando alunos com nota maior ou igual a 7
# Percorra o vetor de notas e informe quantos alunos ficaram com nota maior ou igual a 7.

notas = [8.5, 7.0, 9.2, 6.8, 10.0, 5.5, 7.8]
nota_minima = 7.0
quantidade_aprovados = 0

for nota in notas:
    if nota >= nota_minima:
        quantidade_aprovados += 1

print("Notas da turma:", notas)
print(f"Nota mínima: {nota_minima}")
print(f"Quantidade de alunos com nota maior ou igual a {nota_minima}: {quantidade_aprovados}")
