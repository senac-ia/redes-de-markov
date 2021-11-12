k = 3
modelo_treinado = open("tmp/4.modelo-sugestao.txt", "r")

modelo = {}

for linha in modelo_treinado:
  itens = linha.strip().split("\t")
  entradas = itens[0]
  sugestoes = itens[1].split(",")

  modelo[entradas] = sugestoes

while(True):
  entrada = input("Escreva " + str(k) + " palavras que daremos sugestões. \".\" para sair:\n")
  if entrada == ".":
    break
  palavras = ",".join(map(lambda x: x.strip(" .,;!?/\"\'+-)(:"), entrada.lower().split()))

  if(palavras in modelo):
    print("\nAutosugestão: ")
    print(modelo[palavras])
    print("\n")
  else:
    print("Sem sugestões.\n")
