x: int = 0;
y: int = 0;

x = int(input("Insira o 1o valor: "));
y = int(input("Insira o 2o valor (diferente do 1o): "));

if x == y:
  print("Valores não são diferentes!")
elif x > y:
  print("Valores em ordem:", y, x);
else:
  print("Valores em ordem:", x, y);