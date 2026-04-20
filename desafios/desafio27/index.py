from abc import ABC, abstractmethod
import random
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
import time

console = Console()

class Personagem(ABC):
    def __init__(self, nome, vida_max, golpes):
        self.nome = nome
        self.vida_max = vida_max
        self.vida_atual = vida_max
        self.golpes = golpes  # Dicionário: {"nome_golpe": dano_base}

    def atacar(self, alvo, golpe_nome):
        if golpe_nome in self.golpes:
            dano = self.golpes[golpe_nome] + random.randint(-5, 10)
            console.print(f"[bold yellow]⚔️ {self.nome}[/] usou [cyan]{golpe_nome}[/] em [bold red]{alvo.nome}[/]!")
            alvo.receber_dano(dano)
        else:
            console.print(f"[red]{self.nome} tentou um golpe que não conhece![/]")

    def receber_dano(self, dano):
        self.vida_atual -= dano
        if self.vida_atual < 0:
            self.vida_atual = 0
        console.print(f"💥 [bold red]{self.nome}[/] recebeu [bold]{dano}[/] de dano! (Vida: {self.vida_atual}/{self.vida_max})")

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def curar(self):
        cura = 15
        self.vida_atual = min(self.vida_max, self.vida_atual + cura)
        console.print(f"🛡️ [bold green]{self.nome}[/] usou Recuperação de Fôlego e curou [bold]{cura}[/] de vida!")

class Mago(Personagem):
    def curar(self):
        cura = 25
        self.vida_atual = min(self.vida_max, self.vida_atual + cura)
        console.print(f"✨ [bold blue]{self.nome}[/] usou Magia de Regeneração e curou [bold]{cura}[/] de vida!")

# --- Simulação de Batalha ---

def exibir_status(p1, p2):
    table = Table(title="📊 Status da Batalha")
    table.add_column("Personagem", justify="center", style="bold")
    table.add_column("Classe", justify="center")
    table.add_column("HP", justify="right")

    for p in [p1, p2]:
        cor_hp = "green" if p.vida_atual > (p.vida_max * 0.5) else "red"
        classe = "Guerreiro" if isinstance(p, Guerreiro) else "Mago"
        table.add_row(p.nome, classe, f"[{cor_hp}]{p.vida_atual}/{p.vida_max}[/]")
    
    return table

def iniciar_duelo():
    # Instanciando os heróis
    p1 = Guerreiro("Arthur", 100, {"Corte Rápido": 20, "Impacto Brutal": 35})
    p2 = Mago("Merlin", 80, {"Bola de Fogo": 30, "Raio Arcano": 25})

    console.print(Panel.fit("🔥 [bold red]A BATALHA COMEÇOU![/] 🔥", subtitle="RPG Simulator"))

    turno = 1
    while p1.vida_atual > 0 and p2.vida_atual > 0:
        console.rule(f"Turno {turno}")
        console.print(exibir_status(p1, p2))
        
        # Lógica simples de IA para a simulação
        # Arthur (Guerreiro) ataca
        p1.atacar(p2, random.choice(list(p1.golpes.keys())))
        
        if p2.vida_atual <= 0: break

        # Merlin (Mago) decide se cura ou ataca
        if p2.vida_atual < 30:
            p2.curar()
        else:
            p2.atacar(p1, random.choice(list(p2.golpes.keys())))
        
        turno += 1
        time.sleep(1.5)

    console.rule("FIM DE JOGO")
    vencedor = p1 if p1.vida_atual > 0 else p2
    console.print(Panel(f"🏆 [bold gold1]O VENCEDOR É {vencedor.nome.upper()}![/]", expand=False))

if __name__ == "__main__":
    iniciar_duelo()