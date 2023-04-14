from typing import Type
from entities.Vertex import Vertex
from typing import Optional, Dict, List, Type

class Node():
    def __init__(self, vertex: Type[Vertex],
                 cost: int,
                 vertex_a: Type[Vertex],
                 closed: bool = False):
        self.vertex = vertex
        self.cost = cost
        self.vertex_a = vertex_a
        self.is_closed = closed

    def get_vertex(self) -> Type[Vertex]:
        '''Retorna o vertice do node'''
        return self.vertex
    
    def get_cost(self) -> int:
        '''Retorna o custo para chegar ao node'''
        return self.cost
    
    def get_vertex_ant(self) -> Type[Vertex]:
        '''Retorna o vertice anterior ao selecionado'''
        return self.vertex_a
    
    def get_is_closed(self) -> bool:
        '''Retorna o status do node'''
        return self.is_closed
    
    def set_cost(self, new_cost: int) -> bool:
        '''Valida se o custo é menor, se for ele muda'''
        if new_cost < self.cost:
            self.cost = new_cost
            return True
        return False
        
    def set_vertex_a(self, new_vertex: Type[Vertex]):
        '''Altera o vertex anterior'''
        self.vertex_a = new_vertex

    def set_closed_status(self, status: bool):
        '''Muda o status do node'''
        self.is_closed = status

   