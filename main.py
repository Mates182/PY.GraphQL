from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from typing import List

@strawberry.type
class Movie:
    title: str
    director: str

@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> List[Movie]:
        movies_data = [
            Movie(title="The Silence of the Lambs", director="Jonathan Demme"),
            Movie(title="Lady Snowblood", director="Toshiya Fujita"),
            Movie(title="Pulp Fiction", director="Quentin Tarantino"),
            Movie(title="Scarface", director="Brian De Palma"),
            Movie(title="Fight Club", director="David Fincher"),
        ]
        return movies_data