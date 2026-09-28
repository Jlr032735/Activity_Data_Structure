orders = [
    "P101",
    "CANCELADO",
    "P103",
    "P104",
    "CANCELADO",
    "P106",
    "P107"
]

original_size = len(orders)
removed_cancellations = 0
moviments = 0
changes_index = []

write_index = 0
for read_index in range(original_size):
    if orders[read_index] == "CANCELADO":
        if read_index != write_index:
            changes_index.append((orders[read_index], read_index, write_index))
            moviments += 1
    else:
        removed_cancellations += 1

logic_size = write_index

for i in range(logic_size, original_size):
    if orders[i] == "LIVRE":
        moviments += 1
        orders[i] = "LIVRE"

print(f"Pedidos que mudaram de índice: {[item[0] for item in changes_index]}")
print(f"Cancelamentos eliminados: {removed_cancellations}")
print(f"Movimentações realizadas: {moviments}")
print(f"Tamanho lógico da estrutura: {logic_size}")
print(f"Estrutura reorganizada: {orders}")