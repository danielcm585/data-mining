import pandas as pd


class Node:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.neighbors = []
    
    @property
    def degree(self):
        return len(self.neighbors)

    def add_neighbor(self, node: 'Node'):
        self.neighbors.append(node)
        node.neighbors.append(self)


class DirectedNode(Node):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)
        self.in_neighbors = []
        self.out_neighbors = []

    def add_neighbor(self, node: 'DirectedNode'):
        self.out_neighbors.append(node)
        node.in_neighbors.append(self)

    @property
    def in_degree(self):
        return len(self.in_neighbors)

    @property
    def out_degree(self):
        return len(self.out_neighbors)


class Graph:
    MAX_NODE = 2000

    def __init__(self, csv_file: str, is_directed: bool = False):
        self.is_directed = is_directed
        self.name_to_node = {}
        self.nodes = []
        self.adjacency_matrix = [
            [0]*Graph.MAX_NODE for i in range(Graph.MAX_NODE)
        ]

        df = pd.read_csv(csv_file)
        for index, row in df.iterrows():
            node_1 = self.get_node(row['Node1'])
            node_2 = self.get_node(row['Node2'])
            self.add_edge(node_1, node_2, row['Weight'])
            
    @property
    def num_of_nodes(self):
        return len(self.nodes)
    
    def get_node(self, name: str) -> Node:
        if name not in self.name_to_node:
            if self.is_directed:
                new_node = DirectedNode(len(self.nodes), name)
            else:
                new_node = Node(len(self.nodes), name)
            self.name_to_node[name] = new_node
            self.nodes.append(new_node)
        return self.name_to_node[name]

    def add_edge(self, node_1: Node, node_2: Node, weight: int):
        node_1.add_neighbor(node_2)
        self.adjacency_matrix[node_1.id][node_2.id] = weight
        if not self.is_directed:
            self.adjacency_matrix[node_2.id][node_1.id] = weight

    def get_degree_centrality(self):
        if self.is_directed:
            return (
                [sum([self.adjacency_matrix[j][i] for j in range(len(self.nodes))]) / (len(self.nodes)-1)
                    for i in range(len(self.nodes))],
                [sum(self.adjacency_matrix[i]) / (len(self.nodes)-1)
                    for i in range(len(self.nodes))]
            )

        else:            
            return [
                sum(self.adjacency_matrix[i]) / (len(self.nodes)-1)
                for i in range(len(self.nodes))
            ]


if __name__ == '__main__':
    graph = Graph('graph.csv')