k = 3
grupos = open("tmp/2.k-grupos.txt", "r")

contagem = {}

output = open("tmp/3.contagem.txt", "w")

for grupo in grupos:
  palavras = grupo.strip().split("\t")
  estado = ",".join(palavras[0:-1])
  transicao = palavras[-1]

  if estado not in contagem:
    contagem[estado] = {transicao: 1}
  else:
    if transicao not in contagem[estado]:
      contagem[estado][transicao] = 1
    else:
      contagem[estado][transicao] += 1
    

for estado in contagem:
  soma = 0
  e = contagem[estado]
  for transicao in e:
    soma += e[transicao]
    output.write(estado+"\t"+transicao+"\t"+str(e[transicao])+"\n")
  output.write(estado+"\t"+str(soma)+"\n")