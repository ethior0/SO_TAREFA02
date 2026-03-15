a: float = 0;
b: float = 0;
c: float = 0;
d: float = 0;

print("Atenção! O 1o, 2o e 3o valor precisam estar em ordem crescente!")
a = float(input("Insira o 1o valor: "));
b = float(input("Insira o 2o valor: "));
c = float(input("Insira o 3o valor: "));
d = float(input("Insira o 4o valor: "));

if a > b or b > c:
  print("Os 3 primeiros valores não estão em ordem crescente!");
else:
  print("\nValores ordenados:");
  if d <= a:
    print(d, a, b, c);
  elif d <= b:
    print(a, d, b, c);
  elif d <= c:
    print(a, b, d, c);
  else:
    print(a, b, c, d);