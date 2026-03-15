hIni: int = 0;
hFim: int = 0;
mIni: int = 0;
mFim: int = 0;
sIni: int = 0;
sFim: int = 0;
s: int = 0;
m: int = 0;

hIni = int(input("Insira a hora inicial: "));
mIni = int(input("Insira o minuto inicial: "));
hFim = int(input("Insira a hora final: "));
mFim = int(input("Insira o minuto final: "));

if hIni < 0 or hIni > 23 or hFim < 0 or hFim > 23 or mIni < 0 or mIni > 59 or mFim < 0 or mIni > 59:
  print("Valores fora do limite!");
else:
  # conversão de ambos horários para segundo
  sIni = hIni * 3600 + mIni * 60;
  sFim = hFim * 3600 + mFim * 60;

  if sIni < sFim:
    s = sFim - sIni;
    m = s // 60; # tempo que se passsou em minutos
  else: 
    s = (86400 - sIni) + sFim; # segundos restantes para acabar o dia da hora inicial + segundos do fim do dia até a hora final
    m = s // 60;

  if m // 60 == 24: # caso seja maior que 24 horas
    print("Tempo máximo atingido!");
  else:
    print(f"{m // 60} hora(s) e {m % 60} minuto(s)");