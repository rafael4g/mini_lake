from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from minilake.core import add_beer_to_database, get_beers_from_database

main = typer.Typer(help="Minilake Management Application")

console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database."""
    if add_beer_to_database(name, style, flavor, image, cost):
        print("Beer added to database")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """lists beers in database."""
    beers = get_beers_from_database()
    table = Table(title="Minilake :beer_mug:")
    headers = ["id", "name", "style", "flavor","image","cost","rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        beer.date = beer.date.strftime("%Y-%m-%d")
        values = [
            str(getattr(beer, header)) for header in headers
        ]  # list comprehension
        table.add_row(*values)
    console.print(table)
