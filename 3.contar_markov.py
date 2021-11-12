k = 2
grupos = open("tmp/2.k-grupos.txt", "r")

contagem = {}

for grupo in grupos:
  palavras = grupo.strip().split("\t")
  palavras_estado = palavras[0:-1]
  estado = ",".join(palavras[0:-1])
  transicao = palavras[-1]

  if transicao != "":
    if estado not in contagem:
      contagem[estado] = {transicao: 1}
    else:
      if transicao not in contagem[estado]:
        contagem[estado][transicao] = 1
      else:
        contagem[estado][transicao] += 1
    
output_palavras = open("tmp/3.0.contagem-palavras.txt", "w")
output_estados = open("tmp/3.1.contagem-estados.txt", "w")

output_modelo = open("tmp/4.modelo-sugestao.txt", "w")

for estado in contagem:
  if estado == "": continue
  soma = 0
  e = contagem[estado]
  for transicao in e:
    soma += e[transicao]
    output_palavras.write(estado+"\t"+transicao+"\t"+str(e[transicao])+"\n")
  output_estados.write(estado+"\t"+str(soma)+"\n")

  top_sugestoes = sorted(contagem[estado].items(), key=lambda x: x[1], reverse=True)[0:3]
  top_sugestoes = ",".join(map(lambda x: x[0], top_sugestoes))
  output_modelo.write(estado+"\t"+top_sugestoes+"\n")