# Criando nó com tipos declarados
class Node:
    x: int
    y: int
    key: str

    def __init__(self, key, x, y) -> None:
        self.key = key
        self.x = x
        self.y = y
        return None