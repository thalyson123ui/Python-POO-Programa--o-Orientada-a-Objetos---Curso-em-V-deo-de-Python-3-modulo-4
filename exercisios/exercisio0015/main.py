def exibir_menu():
    print("\n" + "=" * 30)
    print("   SISTEMA DE CADASTRO")
    print("=" * 30)
    print("1. Cadastrar pessoa")
    print("2. Listar pessoas")
    print("3. atualizar pessoa")
    print("4. Excluir pessoa")
    print("5. buscar por nome")
    print("0. Sair")
    print("=" * 30)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            pass  # Aqui você chamaria a função para cadastrar pessoa
        elif opcao == "2":
            pass  # Aqui você chamaria a função para listar pessoas
        elif opcao == "3":
            pass  # Aqui você chamaria a função para atualizar pessoa
        elif opcao == "4":
            pass  # Aqui você chamaria a função para excluir pessoa
        elif opcao == "5":
            pass  # Aqui você chamaria a função para buscar por nome
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()