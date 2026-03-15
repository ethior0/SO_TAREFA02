a: int = 0;
b: int = 0;
res: int = 0;

a = int(input("Insira o primeiro valor: "));
b = int(input("Insira o segundo valor: "));

if a >= b:
  res = a - b;
else:
  res = b - a;

print(f"Resultado: {res}");