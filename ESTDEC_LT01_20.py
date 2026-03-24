import math;

a: float = 0;
b: float = 0;
c: float = 0;
delta: float = 0;
x1: float = 0;
x2: float = 0;

a = float(input("Insira o valor de A: "));
b = float(input("Insira o valor de B: "));
c = float(input("Insira o valor de C: "));

if a == 0:
  print("Não é uma equação de segundo grau!");
else:
  delta = (b * b) - (4 * a * c);

  if delta >= 0:
    x1 = (- b + math.sqrt(delta)) / (2 * a);
    x2 = (- b - math.sqrt(delta)) / (2 * a);
    print(f"Valor das raízes = {{ {x1}, {x2} }}");
  else:
    print("Não há raízes reais");
