def simulate_strategy (initial_record, removal_order):
    record = list(initial_record)
    total_movements = 0
    total_comparisons = 0

    for target in removal_order:
        comparisons = 0
        index = -1
        for i, reg in enumerate(record):
            comparisons += 1
            if reg == target:
                index = i
                break

        total_comparisons += comparisons

        movements = len(record) - 1 - index
        record.pop(index)
        total_movements += movements

    return total_movements, total_comparisons


base_record = ["T01", "T02", "T03", "T04", "T05", "T06", "T07", "T08", "T09", "T10"]

comp_1, desp_1 = simulate_strategy(base_record, ["T09", "T06", "T03"])
comp_2, desp_2 = simulate_strategy(base_record, ["T09", "T03", "T06"])

print(f"Estratégia 1 (Esquerda ---> Direita):")
print(f"- Comparações totais: {comp_1}")
print(f"- Deslocamentos totais: {desp_1}")

print(f"\nEstratégia 2 (Direita ---> Esquerda):")
print(f"- Comparações totais: {comp_2}")
print(f"- Deslocamentos totais: {desp_2}")