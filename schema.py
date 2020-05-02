from typing import List, Union, Iterator

import strawberry  # type: ignore


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class TodoType:
    name: str
    done: bool


todos = [
  TodoType(name="Todo #1", done=False),
  TodoType(name="Todo #2", done=False),
  TodoType(name="Todo #3", done=True)
]


@strawberry.type
class Query:
    @strawberry.field
    def user(self, info) -> List[User]:
        return [User(name="Patrick", age=100)]

    @strawberry.field
    def todos(self, info, done: bool = None) -> Union[List[TodoType], Iterator[TodoType]]:
        if done is not None:
            return filter(lambda todo: todo.done == done, todos)
        else:
            return todos
