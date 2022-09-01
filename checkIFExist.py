
nombreArchivo = "test.txt"
cuenta = 1
with open(nombreArchivo, 'r') as f:
  for line in f:
    print(line + " -- " + str(cuenta))
    cuenta += 1