import numpy as np

class Node:
    def __init__(self, estado_atual, next_estado, valor):
        self.estado = estado_atual
        self.next_estado = next_estado
        self.valor = valor