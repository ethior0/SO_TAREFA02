preco: float = 0;
media: float = 0;
res: float = 0;

preco = float(input("Insira o valor do preço atual: "));
media = float(input("Insira o valor da média mensal: "));

if media < 500 and preco < 30:
  res = preco * 1.1;
elif media >= 500 and media < 1000 and preco >= 30 and preco < 80:
  res = preco * 1.15;
elif media >= 1000 and preco >= 80:
  res = preco * 0.95;
else:
  res = preco;

print(f"Valor do preço novo: R$ {res:.2f}");