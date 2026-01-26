from rich import print
from rich.panel import Panel
from rich.text import Text

# Título do painel
painel_text = Text("Painel de Eventos", style="bold magenta")

# Painel
caixa = Panel(
    "esse é um painel de eventos",
    title=painel_text,
    subtitle="Rodapé do painel",
    subtitle_align="right",
    border_style="blue"
)

print(caixa)
