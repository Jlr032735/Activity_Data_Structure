queue = [
("Aline", 1),
("Bruno", 1),
("Caio", 2),
("Dora", 2),
("Eva", 3)
]

max_capacity = 7
new_passager = ("Felipe", 2)

if len(queue) >= max_capacity:
    print("A fila está cheia. Não é possível adicionar mais passageiros.")
else:
    isersion_position = len(queue)
    for i, (name, priority) in enumerate (queue):
        if priority > new_passager[1]:
            insertion_position = i
            break

deslocate_ellements = [passager[0] for passager in queue[insertion_position:]]
deslocate_quatity = len(deslocate_ellements)

queue.insert(insertion_position, new_passager)

print(f"**Capacidade Disponível:** Sim ({len(queue)}/{max_capacity} vagas ocupadas)")
print(f"**Posição de Inserção de Felipe:** Índice {insertion_position}")
print(f"**Elementos que mudaram de posição:** {deslocate_ellements if deslocate_ellements else 'Nenhum'}")
print(f"**Quantidade total de deslocamentos:** {deslocate_quatity}")
print(f"**Fila Atualizada:** {queue}")
