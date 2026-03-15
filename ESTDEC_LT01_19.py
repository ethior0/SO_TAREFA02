a: float = 0;
b: float = 0;
maior: float = 0;

a = float(input("Insira o primeiro valor: "));
b = float(input("Insira o segundo valor: "));

if a > b:
  maior = a;
  print(f"Maior entre os dois números: {maior}");
elif b > a:
  maior = b;
  print(f"Maior entre os dois números: {maior}");
else:
  print("Ambos os números são iguais");