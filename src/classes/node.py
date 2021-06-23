from typing import Any

# Criando nó com tipos declarados
class Node:
    name: str
    age: int
    key: str

    def __init__(self, key, name, age) -> None:
        self.key = key
        self.name = name
        self.age = age
        return None