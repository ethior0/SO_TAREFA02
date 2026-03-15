tipo: int = 0;
valor: float = 0
novoValor: float = 0;

tipo = int(input("Insira o tipo de investimento (1 = poupança e 2 = renda fixa): "));
valor = float(input("Insira o valor do investimento: "));

if tipo == 1:
  novoValor = (valor * 1.03);
  print(f"R$ {novoValor:.2f}");
elif tipo == 2:
  novoValor = (valor * 1.05)
  print(f"R$ {novoValor:.2f}");
else:
  print("Tipo inválido!");
