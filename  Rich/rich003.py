from rich import print
from rich.table import Table

table = Table(title="Star Wars Movies")
table.add_column("Title", style="cyan", no_wrap=True)
table.add_column("Director", style="magenta")
table.add_column("Release Year", justify="right", style="green")
table.add_column("Box Office (in billions)", justify="right", style="yellow")
table.add_row("A New Hope", "George Lucas", "1977", "0.775")
table.add_row("The Empire Strikes Back", "Irvin Kershner", "1980", "0.538")
table.add_row("Return of the Jedi", "Richard Marquand", "1983", "0.475")
table.add_row("The Phantom Menace", "George Lucas", "1999", "1.027")
table.add_row("Attack of the Clones", "George Lucas", "2002", "0.649")
table.add_row("Revenge of the Sith", "George Lucas", "2005", "0.848")
table.add_row("The Force Awakens", "J.J. Abrams", "2015", "2.068")
table.add_row("The Last Jedi", "Rian Johnson", "2017", "1.332")
table.add_row("The Rise of Skywalker", "J.J. Abrams", "2019", "1.074")
print(table)