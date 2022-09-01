import os
import urllib2

# if os.name != 'nt':
  
nombreArchivo = "test.txt"
cuenta = 1
with open(nombreArchivo, 'r') as f:
  for line in f:
    
    
    if check(line):
      print(str(cuenta))
    
    
    
    
    
    
    
    
    
    
    # if line != "":




      # cadena = 'wget -O/dev/null -q ' + line
      # if not os.system(cadena):
      #   print(str(cuenta))
      # print(line + " -- " + str(cuenta))
    cuenta += 1
# else:
#   print("Upsss, este script está diseñado para linux... :v")

def check(url):
  try:
    urllib2.urlopen(url)
    return True
  except urllib2.HTTPError:
    return False
