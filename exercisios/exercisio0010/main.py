from exercisio0010 import Cachorro, Gato, Galinha

def main():
    a = Cachorro("Quiara")
    b = Gato("Lili")
    c = Galinha("Cláudia")
    
    a.emitir_som()
    b.emitir_som()
    c.emitir_som()

if __name__ == "__main__":
    main()