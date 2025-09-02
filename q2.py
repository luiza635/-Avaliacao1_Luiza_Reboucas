quantidade = int(input("Quantos produtos foram vendidos? "))
produtos = []

for i in range(quantidade):
    valor = float(input(f"Valor do produto {i+1}: "))
    produtos.append(valor)

total = sum(produtos)
maior_50 = sum(1 for v in produtos if v > 50)
menor_50 = sum(1 for v in produtos if v < 50)

print(f"\nValor total: R$ {total:.2f}")
print(f"Produtos com o valor{maior_50}")
print(f"Produtos com o valor{menor_50}")