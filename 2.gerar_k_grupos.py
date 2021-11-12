palavras = open("tmp/1.palavras.txt", "r")

k = 3

lista = [""]*k

output = open("tmp/2.k-grupos.txt", "w")

for palavra in palavras:
  lista.insert(0, palavra.strip())
  del lista[-1]
  if lista[1] != "" or lista[2] != "":
    output.write("\t".join(lista) + "\n")
print("Acabou")