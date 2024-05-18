'''
    Graph class

    This will be fully type annotated after MyPy supported generic classes.  The
    main issue for now is that we need to Any for the Vertex type parameter.
'''

from typing import TypeAlias
from typing import Any

Edge: TypeAlias = tuple[Any, Any, float]
''' type: Edge = tuple[Any, Any, float] '''

AdjList: TypeAlias = dict[Any, list[Edge]]
''' type: AdjList = dict[Any, Edge]'''

class Graph:
    ''' Represents a graph using an adjacency list'''

    def __init__(self, directed: bool) -> None:
        self._directed = directed
        self._num_edges = 0
        self._adj: AdjList = {}

    def add_edge_to_adj(self, v: Any, edge: Edge) -> None:
        ''' Add an edge to the adjacency list.'''
        if v in self._adj:
            self._adj[v].append(edge)
        else:
            self._adj[v] = [edge]

    def add_edge(self, v_from: Any, v_to: Any, weight: float) -> None:
        ''' Add edge from v_from to v_to, with given weight '''
        edge: Edge = (v_from, v_to, weight)
        if v_from not in self._adj:
            self._adj[v_from] = []
        if v_to not in self._adj:
            self._adj[v_to] = []
        self._adj[v_from].append(edge)
        if not self._directed:
            self._adj[v_to].append(edge)
        self._num_edges += 1

    def adj(self, v: Any) -> list[Edge]:
        ''' Return the adjacency list for the given vertex '''
        if v in self._adj:
            return self._adj[v][:]
        else:
            return []

    def __str__(self):
        return str(self._adj)
