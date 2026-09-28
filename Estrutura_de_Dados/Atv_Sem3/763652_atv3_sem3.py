reads = [23.4, 24.1, 25.0, 27.8, 31.6, 33.2]
critical_limit = 30.0

found_value = False
found_index = -1
comparation = 0

for i, temperature in enumerate(reads):
    comparation += 1
    if temperature > critical_limit:
        found_value = temperature
        found_index = i
        break

if found_value is not None:
    percentage_completed = (comparation / len(reads)) * 100
    print(f"Valor encontrado: {found_value} °C")
    print(f"Índice: {found_index}")
    print(f"Comparações necessárias: {comparation}")
    print(f"Percentual percorrido: {percentage_completed:.1f}%")

else:
    print("Nenhuma leitura critica encontrada acima do limite.")
