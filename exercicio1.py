from datetime import date

"""
Faça um programa que leia a idade de uma pessoa expressa em dias e
mostre-a expressa em anos, meses e dias.
"""
#DATA ATUAL
hoje = date.today()
anoAtual= hoje.strftime("%Y")
mesAtual= hoje.strftime("%m")
diaAtual= hoje.strftime("%d")

#DATA NASCIMENTO
dia = int(input("DIGITE O DIA DO NASCIMENTO: "))
mes = int(input("DIGITE O MES DO NASCIMENTO: "))
ano = int(input("DIGITE O ANO DO NASCIMENTO: "))

#converte data atual em InterruptedError
anoAtual=int(anoAtual)
mesAtual=int(mesAtual)
diaAtual=int(diaAtual)

#CALCULO IDADE
resultAno = anoAtual - ano
resultMes = mesAtual - mes
resultDia = diaAtual - dia

print ("Voce tem %i anos, %i meses e %i dias" % (resultAno,resultMes,resultDia))
