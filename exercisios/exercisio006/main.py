from exercisios.exercisio003.exercisio003 import contabancaria

def main():
    conta = contabancaria("Thalyson", 1234)
    conta.exibir_dados()
    conta.depositar(500)
    conta.sacar(200)
    conta.exibir_dados()

if __name__ == "__main__":
    main()
