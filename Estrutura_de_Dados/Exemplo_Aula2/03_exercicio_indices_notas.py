# Exercício 03 - Mostrando notas com seus índices
# Mostre todas as notas acompanhadas de seus respectivos índices.

notas = [8.5, 7.0, 9.2, 6.8, 10.0]

print("Notas da turma com seus índices:")

for indice, nota in enumerate(notas):
    print(f"Índice {indice} -> Nota {nota}")
