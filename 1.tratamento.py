machado = ["casaVelha.txt", "domCasmurro.txt", "esau.txt", "iaia.txt", "memorial-de-aires.txt", "memoriasBras.txt", "quincas.txt"]

stopwords = ["-", "—"]

output = open("tmp/1.palavras.txt", "w")

for livro in machado:
  print("Tratando livro: " + livro)
  for linha in open("treinamento/"+livro, "r"):
    palavras = linha.lower().split()
    for palavra in palavras:
      palavra = palavra.strip(" .,;!?/\"\'+-)(:")

      if palavra not in stopwords:
        output.write(palavra + "\n")

print("Acabou")
