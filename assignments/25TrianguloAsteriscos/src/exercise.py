
def main():
    #Escribe tu código debajo de esta línea
    n = int(input("Height of the triangle: "))
    b = 0
    a = n
    while b<n:
        b = b+1
        a = n-b
        print((a*" "),("*"*b))
        if b>=n:
            break

    pass


if __name__=='__main__':
    main()
