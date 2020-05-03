from typing import List, Union, Iterator, Optional

import strawberry  # type: ignore


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Todo:
    name: str
    done: bool


_todos = [
  Todo(name="Todo #1", done=False),
  Todo(name="Todo #2", done=False),
  Todo(name="Todo #3", done=True)
]


@strawberry.type
class Query:
    @strawberry.field
    def user(self, info) -> List[User]:
        return [User(name="Patrick", age=100)]

    @strawberry.field
    def todos(self, info, done: bool = None) -> List[Todo]:
        if done is None:
            return _todos
        return list(filter(lambda todo: todo.done == done, _todos))
