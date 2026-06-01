def esPrimo(num):
    primo = True
    for x in range( 2,num ):
        if num % x == 0:
            primo = False
    return primo
