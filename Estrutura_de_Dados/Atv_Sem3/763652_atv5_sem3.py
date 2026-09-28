tasks = [
    "Backup",
    "Atualizar BD",
    "Reiniciar API",
    "Teste"
]

max_capacity = 6
total_displacements = 0

restart_index = -1
for i, task in enumerate(tasks):
    if task == "Reiniciar API":
        restart_index = i
        break

tasks.insert(restart_index, "Patch critico")
total_displacements += len(tasks) - 1 -restart_index

renew_index = -1
for i, task in enumerate(tasks):
    if task == "Atualizar BD":
        renew_index = i
        break

tasks.pop(renew_index)
total_displacements += len(tasks) - renew_index

if len(tasks) < max_capacity:
    tasks.append("Gerar Relatorio")

logic_size = len(tasks)
remaining_capacity = max_capacity - logic_size

print(f"**Agenda Reorganizada:** {tasks}")
print("**Índices de cada elemento:**")
for i, task in enumerate(tasks):
    print(f"- Índice {i}: {task}")
print(f"Tamanho Lógico: {logic_size}")
print(f"Capacidade Restante: {remaining_capacity}")
print(f"Quantidade Total de Deslocamentos: {total_displacements}")