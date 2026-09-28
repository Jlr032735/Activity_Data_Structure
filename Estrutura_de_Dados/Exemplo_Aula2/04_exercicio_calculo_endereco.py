# Exercício 04 - Simulando cálculo de endereço
# Simule o cálculo do endereço de uma posição do vetor,
# considerando endereço base 3000 e tamanho de elemento 8 bytes.

endereco_base = 3000
tamanho_elemento = 8
indice = int(input("Digite o índice da posição desejada: "))

endereco = endereco_base + (indice * tamanho_elemento)

print("\nCálculo conceitual de endereço")
print(f"Endereço base: {endereco_base}")
print(f"Índice informado: {indice}")
print(f"Tamanho do elemento: {tamanho_elemento} bytes")
print(f"Endereço calculado: {endereco}")
