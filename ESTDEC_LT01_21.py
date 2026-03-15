n1: float = 0;
n2: float = 0;
n3: float = 0;
n4: float = 0;
media: float = 0;

n1 = float(input("Insira a 1a nota: "));
n2 = float(input("Insira a 2a nota: "));
n3 = float(input("Insira a 3a nota: "));
n4 = float(input("Insira a 4a nota: "));

if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10 or n4 < 0 or n4 > 10:
  print("Valores fora do limite! (0-10)");
else:
  media = (n1 + n2 + n3 + n4) / 4;
  print(media);
  if media >= 6:
    print("Aprovado");
  elif media >= 3:
    print("Exame");
  else:
    print("Retido");