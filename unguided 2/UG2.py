import time
import matplotlib

def ini_bil_prima(x):
  for i in range(2, x):
    if x % i == 0:
      return False

  return True

def deretprima_it(n):
    list_bil_prima = []
    for i in range(1, n+1):
        if ini_bil_prima(x):
            list_bil_prima.append(x)
    return list_bil_prima

def deretprima_rk(n):
    if n == 100:
        return 1
    else:
        return n * deretprima_rk(n-1)
      


hasil1 = deretprima_it(100)
print('Deret Bilangan Prima sebanyak 100 dengan cara iteratif: ', hasil1)
hasil2 = deretprima_rk(100)
print('Deret Bilangan Prima sebanyak 100 dengan cara rekursif: ', hasil2)