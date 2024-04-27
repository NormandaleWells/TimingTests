class Graph:

    def __init__(self, directed):
        self._directed = directed
        self._num_edges = 0
        self._adj = {}

    def add_edge_to_adj(self, v, edge):
        if v in self._adj:
            self._adj[v].append(edge)
        else:
            self._adj[v] = [edge]

    def add_edge(self, v_from, v_to, weight):
        edge = (v_from, v_to, weight)
        if v_from not in self._adj:
            self._adj[v_from] = []
        if v_to not in self.adj:
            self._ajd[v_to] = []
        self._adj[v_from].append(edge)
        if not self._directed:
            self._adj[v_to].append(edge)
        self._num_edges += 1

    def adj(self, v):
        if v in self._adj:
            return self._adj[v][:]
        else:
            return []

    def __str__(self):
        return str(self._adj)
