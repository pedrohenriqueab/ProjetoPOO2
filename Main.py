from Questao1.Model import *
def main():
    a1 = Animal("max", 3, "casa")
    print (a1)

    rex = Cachorro("rex", 5, "house", "labrador")
    print(rex)
    rex.vigiar()

    blublu = Peixe("blublu", 2, "aquario", "triangular")
    print(blublu)

if (__name__=='__main__'):
    main()