import classes

def main():
    a = classes.Porta()
    b = classes.Empresa()
    c = classes.Ovo()
    d = classes.Pedra()

    classes.tentar_abrir(a)
    classes.tentar_abrir(b)
    classes.tentar_abrir(c)
    classes.tentar_abrir(d)

if __name__ == "__main__":
    main()