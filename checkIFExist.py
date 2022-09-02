from urllib.request import urlopen
from urllib.error import URLError
from urllib.parse import urlparse

def check(url):
  try:
    urlopen(url)
    return True
  except URLError:
    return False
def vacio(x):
  if x == "\n":
    return True
  else:
    return False
  
nombreArchivo = "test.txt"
cuenta = 1
with open(nombreArchivo, 'r') as f:
  for line in f:
    if vacio(line):
      print("linea vacia: " + str(cuenta))
    else:
      if not check(line):
        print("no existe: " + str(cuenta))
    cuenta += 1
