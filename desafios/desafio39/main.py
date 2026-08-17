from abc import ABC, abstractmethod
import re

class Validador(ABC):
    """Classe abstrata base para os validadores de dados."""
    
    @abstractmethod
    def validar(self, valor: str) -> bool:
        """Método abstrato que deve ser implementado por cada validador."""
        pass


class ValidadorUsuario(Validador):
    """Valida nomes de usuário: 3 a 20 caracteres (letras, números, _ ou -)."""
    
    PADRAO = r"^[a-zA-Z0-9_-]{3,20}$"

    def validar(self, valor: str) -> bool:
        return bool(re.match(self.PADRAO, valor))


class ValidadorEmail(Validador):
    """Valida e-mails no formato padrão usuario@dominio.extencao."""
    
    PADRAO = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    def validar(self, valor: str) -> bool:
        return bool(re.match(self.PADRAO, valor))


class ValidadorSenha(Validador):
    """
    Valida senhas fortes:
    - Mínimo de 8 caracteres
    - Pelo menos 1 letra maiúscula
    - Pelo menos 1 letra minúscula
    - Pelo menos 1 número
    - Pelo menos 1 caractere especial (@$!%*?&)
    """
    
    PADRAO = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    def validar(self, valor: str) -> bool:
        return bool(re.match(self.PADRAO, valor))


# --- Demonstração de Uso ---
if __name__ == "__main__":
    testes = {
        "Usuário": (ValidadorUsuario(), ["dev_user99", "ab", "user@name"]),
        "E-mail": (ValidadorEmail(), ["contato@empresa.com", "email-invalido@.com"]),
        "Senha": (ValidadorSenha(), ["Senha@123", "12345678", "senhafraca"]),
    }

    for categoria, (validador, entradas) in testes.items():
        print(f"--- Validando {categoria} ---")
        for entrada in entradas:
            resultado = "Válido" if validador.validar(entrada) else "Inválido"
            print(f"'{entrada}': {resultado}")