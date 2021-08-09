# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:34:46 2018

@author: aicha
"""
import math 
from fractions import *
"""liste de quotients partiels"""
from fractions import *
import math 
def DevContinuedFraction(num, denum) :
   partialQuotients = []
   divisionRests = []
   for i in range(int(math.log(denum, 2)/1)) :
       divisionRests = num % denum
       partialQuotients.append(int (num / denum))
       num = denum
       denum = divisionRests
       if denum == 0 :
           break
       print(Fraction(num,denum))
       print("quotinets partiels")
       print( partialQuotients )
   return  partialQuotients 
"""liste de convergence ou reduite"""
def DivergentsComputation(num,denum ) :
   partialQuotients=DevContinuedFraction(num, denum)
   print("recherche de d < (1/3)*pow(n,0.25) en cours ....")
   test =(1/3)*pow(denum,0.25)
   print (test)    
   (p1, p2, q1, q2) = (1, 0, 0, 1)
   convergentsList = []
   for q in partialQuotients :
       pn = q * p1 + p2
       qn = q * q1 + q2
       convergentsList.append([pn, qn])
       p2 = p1
       q2 = q1
       p1 = pn
       q1 = qn
       while qn<test:
           print( convergentsList ) 
           k=pn
           d=qn
           print("valeur de k:")
           print(k)
           print("valeur de  d :")
           print(d)
           break
   print ([d,k]) 
   return ([d,k]) 
"""racine carre """
def find_invpow(x,n):
   high = 1
   while high ** n < x:
       high *= 2
   low = high/2
   while low < high:
       mid = (low + high) // 2
       if low < mid and mid**n < x:
           low = mid
       elif high > mid and mid**n > x:
           high = mid
       else:
           return mid
   return mid + 1
"""solution de lequation deuxieme degree"""

if __name__ == "__main__":
     n = 2630048851947048265274043876774585976831617720728227254753421
     e = 60177566799353897687038964037333604046539474788802464201235
     [d,k]=DivergentsComputation(e, n)
     print("calcule de phi")
     up=e*d-1
     phi=int(up/k)
     print(phi)
     b = phi-n-1
     delta =b*b - 4*n
     print("calcule de p")
     print(int((-b + find_invpow((delta), 2))/(2)))
     print("calcule de q")
     print(int(-1*(-b - find_invpow((delta), 2))/(2)))