import hashlib

class ContaBancaria:
    def __init__(self, id_conta, titular, senha_inicial, nome_exibicao):
        # Atributos Protegidos (Convenção: 1 underline)
        self._id = id_conta
        self._titular = titular
        
        # Atributos Privados (Encapsulamento forte: 2 underlines)
        self.__saldo = 0.0
        # Guardamos a senha criptografada em um hash MD5 para segurança
        self.__hash = hashlib.md5(senha_inicial.encode()).hexdigest()
        
        # Atributo Público
        self.nome = nome_exibicao

    # --- MÉTODOS PÚBLICOS DE VALIDAÇÃO ---
    def validar_senha(self, chave):
        """Verifica se a senha digitada confere com o hash guardado."""
        hash_tentativa = hashlib.md5(chave.encode()).hexdigest()
        return hash_tentativa == self.__hash

    def pede_senha(self):
        """Solicita a senha no terminal e já valida."""
        tentativa = input("Digite a sua senha: ")
        if self.validar_senha(tentativa):
            return True
        print("❌ Senha incorreta!")
        return False

    # --- MÉTODOS PÚBLICOS DE OPERAÇÃO BANCÁRIA ---
    def depositar(self, valor):
        """Permite depositar dinheiro. Não exige senha."""
        if valor > 0:
            self.__saldo += valor
            print(f"💰 Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("❌ Valor de depósito inválido.")

    def sacar(self, valor, chave):
        """Permite sacar dinheiro se a senha for válida e houver saldo."""
        if self.validar_senha(chave):
            if 0 < valor <= self.__saldo:
                self.__saldo -= valor
                print(f"💸 Saque de R${valor:.2f} realizado com sucesso!")
                return True
            else:
                print("❌ Saldo insuficiente ou valor inválido.")
                return False
        else:
            print("❌ Senha incorreta! Operação cancelada.")
            return False

    # --- GETTER PARA EXIBIÇÃO SEGURA DO SALDO ---
    def ver_saldo(self):
        """Apenas permite ver o saldo após pedir a senha."""
        if self.pede_senha():
            print(f"💵 Saldo atual de {self.nome}: R${self.__saldo:.2f}")
        _ = """Método auxiliar para visualização"""


# ==========================================
# TESTANDO A CLASSE (SIMULAÇÃO DO BANCO)
# ==========================================
if __name__ == "__main__":
    print("--- Criando a conta do Guanabara ---")
    # Criando a conta com ID, Titular, Senha ("1234") e Nome de exibição
    conta = ContaBancaria(101, "Gustavo G. Guanabara", "1234", "Guanabara")

    print(f"\nNome público da conta: {conta.nome}")
    
    # 1. Tentando acessar o saldo diretamente (Vai dar erro se tentar)
    # print(conta.__saldo) # Se desmarcar essa linha, o Python bloqueia e dá AttributeError!
    
    # 2. Fazendo um depósito
    print("\n--- Depositando ---")
    conta.depositar(500.00)

    # 3. Tentando ver o saldo (pede senha)
    print("\n--- Consultando Saldo ---")
    conta.ver_saldo()

    # 4. Tentando sacar com a senha errada
    print("\n--- Tentativa de Saque (Senha Errada) ---")
    conta.sacar(100.00, "9999")

    # 5. Tentando sacar com a senha certa
    print("\n--- Tentativa de Saque (Senha Certa) ---")
    conta.sacar(150.00, "1234")

    # 6. Consultando saldo final para checar o resultado
    print("\n--- Consultando Saldo Final ---")
    conta.ver_saldo()