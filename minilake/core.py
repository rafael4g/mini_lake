from typing import List, Optional

# from sympy import im
from sqlmodel import select

from minilake.database import get_session
from minilake.models import Minilake


def add_beer_to_database(
    name: str,
    style: str,
    flavor: int,
    image: int,
    cost: int,
) -> bool:
    with get_session() as session:
        beer = Minilake(**locals())
        session.add(beer)  # INSERT INTO
        session.commit()

    return True


def get_beers_from_database(style: Optional[str] = None) -> List[Minilake]:
    with get_session() as session:
        sql = select(Minilake)
        if style:
            sql = sql.where(Minilake.style == style)
        return list(
            session.exec(sql)
        )  # utilizar sem a list para performance e paginação
