from typing import List, Optional

from fastapi import (  # protocolo ASGI: Assing server getway interface ( modern python )
    FastAPI,
    Response,
    status,
)

from minilake.core import get_beers_from_database
from minilake.database import get_session
from minilake.models import Minilake
from minilake.serializers import MinilakeIn, MinilakeOut

api = FastAPI(title="Minilake")


@api.get("/beers/", response_model=List[MinilakeOut])
async def list_beers(style: Optional[str] = None):
    """Lists beers from the database"""
    beers = get_beers_from_database(style)
    return beers


@api.post("/beers/", response_model=MinilakeOut)
async def add_beer(beer_in: MinilakeIn, response: Response):
    beer = Minilake(**beer_in.dict())
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer)
    response.status_code = status.HTTP_201_CREATED
    return beer
