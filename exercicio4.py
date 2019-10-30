for nr in range(2,100):

    print(nr, end=' - >')

    primo = True
    x = 2
    while x < nr and primo:
        if nr %x == 0:
            primo = False
        x+=1

    if primo:
      print("VERDADEIRO")
    else:
        print ("FALSO")
