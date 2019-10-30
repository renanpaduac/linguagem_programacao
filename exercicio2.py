x = int(input("DIGITE UM VALOR PARA X: "))
y = int(input("DIGITE UM VALOR PARA Y: "))
z = int(input("DIGITE UM VALOR PARA Z: "))

if x>=y+z or y>=z+x or z>=x+y :
    print ("Triangulo Inexistente")
    quit()

if x==y and y==z :
    print ("Tringulo Equilatero")

elif x==y or y==z or z==x :
    print ("Tringulo Isosceles")
    
else:
  print ("Tringulo Escaleno")
