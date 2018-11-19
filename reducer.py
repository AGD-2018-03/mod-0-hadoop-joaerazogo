#!/usr/bin/env python

import sys

##
## Esta función reduce los elementos que 
## tienen la misma clave
##

if __name__ == '__main__': 
  
    curkey = None
    total = 0
    suma = 0
    totalNum = 0
    
    ##
    ## cada linea de texto recibida es una 
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:
        
        key, val, num= line.split('\t') 
        val = int(val)
        num = int(num)
        
        if key == curkey:
            total += val
            totalNum = totalNum + num
        else:
            ##
            ## Se cambio de clave. Se reinicia el
            ## acumulador.
            ##
            if curkey is not None:
                
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, float(total), float(total)/float(totalNum))) 
                ##
                ## una vez se han reducido todos los elementos
                ## con la misma clave se imprime el resultado en
                ## el flujo de salida
                ##
            totalNum = num
            curkey = key
            total = val
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, float(total), float(total)/float(totalNum))) 