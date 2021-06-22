from typing import Any

# Criando nó com tipos declarados
class Node:
    name: str
    age: int

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        pass