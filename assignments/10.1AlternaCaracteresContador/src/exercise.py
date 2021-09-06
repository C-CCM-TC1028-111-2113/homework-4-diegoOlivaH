def main():
    #escribe tu código abajo de esta línea
    n = int(input("Number: "))
    b = 0
    while b<n:
        b = b+1
     if (b%2==0):
        print(b," - %")
      if not(b%2==0):
        print(b," - #")
        
    pass

if __name__=='__main__':   
    main()
