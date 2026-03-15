voltas: int = 0;
tempo: int = 0; # minutos
extensao: float = 0; # em metros
velMs: float = 0;
velKm: float = 0;

voltas = int(input("Insira o número de voltas: "));
tempo = int(input("Insira o tempo de duração (em minutos): "));
extensao = float(input("Insira a extensão do circuito (em metros): "));

velMs = (voltas * extensao) / (tempo * 60);
velKh = velMs / 3.6;

print(f"Velocidade: {velKh:.3f} km/h");