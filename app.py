import strawberry  # type: ignore

from schema import Query

schema = strawberry.Schema(query=Query)
