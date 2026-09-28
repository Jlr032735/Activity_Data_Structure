# Exercício 01 - Acessando posições específicas do vetor
# Crie um vetor com as notas de 6 alunos e exiba a nota do primeiro, do terceiro e do último aluno.

notas = [8.5, 7.0, 9.2, 6.8, 10.0, 7.5]

primeira_nota = notas[0]
terceira_nota = notas[2]
ultima_nota = notas[-1]  # também poderia ser notas[len(notas) - 1]

print("Vetor de notas:", notas)
print("Nota do primeiro aluno:", primeira_nota)
print("Nota do terceiro aluno:", terceira_nota)
print("Nota do último aluno:", ultima_nota)
