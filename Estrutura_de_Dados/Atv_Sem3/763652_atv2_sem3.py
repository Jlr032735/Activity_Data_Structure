queue = [
    ["Rui", 1],
    ["Noah", 2],
    ["Sara", 3],
    ["Olga", 3],
    ["Lia", 4],
]

target_pacients = "Sara"
new_priority = 1

comparisons_count = 0
old_index = -1
for index, (name, priority) in enumerate(queue):
    comparisons_count += 1
    if name == target_pacients:
        old_index = index
        break

removed_pacient = queue.pop(old_index)
removed_pacient[1]= new_priority

removal_displacements = len(queue) - old_index

insertion_index = len(queue)
for index, (name, priority) in enumerate(queue):
    if priority > new_priority:
        insertion_index = index
        break

insertion_displacements = len(queue) - insertion_index
queue.insert(insertion_index, removed_pacient)

total_movements = removal_displacements + insertion_displacements

print(f"Comparações para localizar o paciente: {comparisons_count}")
print(f"Deslocamentos causados pela remoção: {removal_displacements}")
print(f"Deslocamentos causados pela inserção: {insertion_displacements}")
print(f"Custo total em movimentações: {total_movements}")
print(f"Fila Atualizada: {queue}")