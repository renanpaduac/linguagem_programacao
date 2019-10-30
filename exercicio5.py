import string

x = string.ascii_letters
y = x[1:] + x[0]
tabela = string.maketrans(x,y)

mensagem = "o cruzeiro nao ira cair para serie b"

print string.translate(mensagem,tabela)
