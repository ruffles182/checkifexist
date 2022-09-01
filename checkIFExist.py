import os

if os.name != 'nt':
  
  nombreArchivo = "test.txt"
  cuenta = 1
  with open(nombreArchivo, 'r') as f:
    for line in f:
      if line != "":
        cadena = 'wget -O/dev/null -q ' + line + ' && echo \n  || echo ' + str(cuenta)
        os.system(cadena)
        # print(line + " -- " + str(cuenta))
      cuenta += 1
else:
  print("Upsss, este script está diseñado para linux... :v")
