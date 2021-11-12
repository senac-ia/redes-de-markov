import random
k = 2
contagem_estados = open("tmp/3.1.contagem-estados.txt", "r")
contagem_palavras = open("tmp/3.0.contagem-palavras.txt", "r")

modelo = {}

for contagem_palavra in contagem_palavras:
  estado,palavra,contagem = contagem_palavra.strip().split("\t")
  if estado not in modelo: modelo[estado] = {}
  modelo[estado][palavra] = int(contagem)

for contagem_estado in contagem_estados:
  estado,contagem = contagem_estado.strip().split("\t")
  contagem = int(contagem)
  step = 0.0
  for palavra in modelo[estado]:
    frequency = step + (modelo[estado][palavra] * 1.0/contagem)
    modelo[estado][palavra] = (step, frequency)
    step = frequency

def sorteia(estado):
  n = random.random()

  for palavra, v in estado.items():
    if n >= v[0] and n <= v[1]: return palavra

while(True):
  entrada = input("Escreva " + str(k) + " que produziremos um parágrafo com 20 palavras. \".\" para sair:\n")

  if entrada == ".":
    break

  palavras = ",".join(map(lambda x: x.strip(" .,;!?/\"\'+-)(:\n\t"), entrada.lower().split()))
  print(palavras)

  if(palavras in modelo):
    print("\nAutosugestão: ")
    
    print(sorteia(modelo[palavras]))
    print("\n")
  else:
    print("Sem sugestões.\n")