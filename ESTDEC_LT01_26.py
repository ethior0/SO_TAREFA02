x: int = 0;
y: int = 0;
maior: int = 0;
menor: int = 0;

x = int(input("Insira o 1o número: "));
y = int(input("Insira o 2o número: "));

if x > y:
  maior = x;
  menor = y;
else:
  maior = y;
  menor = x;

if maior % menor == 0:
  print("É múltiplo");
else:
  print("Não é múltiplo");