import crud

def exibir_menu():
    print("\n" + "=" * 30)
    print("   SISTEMA DE CADASTRO")
    print("=" * 30)
    print("1. Cadastrar pessoa")
    print("2. Listar pessoas")
    print("3. Atualizar pessoa")
    print("4. Excluir pessoa")
    print("5. Buscar por nome")
    print("0. Sair")
    print("=" * 30)

def main():
    if not crud.criar_banco():
        print("Falha ao criar o banco de dados. Encerrando o programa.")
        raise SystemExit

    # Descomente a linha abaixo apenas se quiser popular o banco na primeira execução:
    # crud.cadastro_em_massa()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            crud.cadastrar_pessoa()
        elif opcao == "2":
            crud.listar_pessoas()
        elif opcao == "3":
            crud.atualizar_pessoa()
        elif opcao == "4":
            crud.excluir_pessoa()
        elif opcao == "5":
            crud.buscar_por_nome()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()