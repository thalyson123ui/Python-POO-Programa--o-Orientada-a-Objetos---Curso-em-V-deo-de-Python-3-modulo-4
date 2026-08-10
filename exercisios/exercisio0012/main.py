from classes import Carteira

def main():
    c1 = Carteira(100)
    c2 = Carteira(200)

    c1 += 50
    c1 += 100.50

    if c1 == c2:
        print("As carteiras são iguais")
    else:
        print("As carteiras são diferentes")


if __name__ == "__main__":
    main()