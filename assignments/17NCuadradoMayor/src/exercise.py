

def main():
    #Escribe tu código debajo de esta línea
    n = int(input("Number: "))
    v = 1
    s = int()
    while s<=n:
        v = v + 1
        s = v**2
        if s>n:
            print(v)

    pass

if __name__=='__main__':
    main()
