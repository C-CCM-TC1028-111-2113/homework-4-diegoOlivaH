
def main():
    #escribe tu código abajo de esta línea
    n = int(input("Enter a number: "))
    a = 0
    b = 1
    c = int()
    d = 1
    if n==0:
        print(a)
    while d<n:
        c = b + a
        a = b
        b = c
        d += 1
        if d>=n:
            print(c)
    pass

if __name__=='__main__':
    main()
