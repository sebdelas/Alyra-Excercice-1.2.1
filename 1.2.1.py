#!/usr/bin/env python3

def calcul_factoriel(nb, factoriel):
   if (nb > 1):      
      nb = nb - 1
      factoriel = factoriel * nb
      return calcul_factoriel(nb, factoriel)
   else:
      return factoriel

nb = int(input("Saisissez un nombre : "))
factoriel = calcul_factoriel(nb, nb)
print ("La factoriel de " + str(nb) +  " est " + str(factoriel))
