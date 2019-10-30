nr1 = int(input("DIGITE UM NUMERO: "))
nr2 = int(input("DIGITE UM OUTRO NUMERO: "))
nr3 = int(input("DIGITE MAIS UM NUMERO: "))

menor = nr1

if menor > nr2:
  menor = nr2
if menor > nr3:
  menor = nr3

print ("Menor Valor foi: %d" % (menor) )
