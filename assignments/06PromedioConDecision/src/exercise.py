def prom(x,y):
    x = x
    y = y
    Prom = x/y
    return Prom

def main():
    #escribe tu código abajo de esta línea
    n = float()
    b = 0
    Sum = 0
    while n >=0:
        n = float(input("Number: "))
        if n>=0:
            Sum += n
            b = b+1
        if n<0:
            print (prom(Sum,b))

    pass

if __name__=='__main__':
    main()
