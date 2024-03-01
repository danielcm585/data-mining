import pandas as pd
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from typing import List


class Node:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.neighbors = []
    
    def __lt__(self, other: 'Node'):
        return self.name < other.name

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
    INFINITY = int(1e18)

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

    def get_shortest_path(self, start: str) -> List[int]:
        try:
            start_node = self.name_to_node[start]
        except:
            raise KeyError('Start node not valid')

        dist = [Graph.INFINITY] * len(self.nodes)
        pq = []
        
        dist[start_node.id] = 0
        heapq.heappush(pq, [0, start_node])

        while len(pq) > 0:
            cur_dist, cur_node = heapq.heappop(pq)
            if dist[cur_node.id] != cur_dist:
                continue
            for nx_node in cur_node.out_neighbors:
                weight = self.adjacency_matrix[cur_node.id][nx_node.id]
                if dist[nx_node.id] > cur_dist + weight:
                    print(f"{cur_node.name} ke {nx_node.name}")
                    dist[nx_node.id] = cur_dist + weight
                    heapq.heappush(pq, [dist[nx_node.id], nx_node])

        return dist

    def visualize(self):
        G_nx = nx.DiGraph() if self.is_directed else nx.Graph()

        for node in self.nodes:
            G_nx.add_node(node.name)

            for neighbor in (node.out_neighbors if self.is_directed else node.neighbors):
                if not G_nx.has_edge(node.name, neighbor.name):
                    weight = self.adjacency_matrix[node.id][neighbor.id]
                    G_nx.add_edge(node.name, neighbor.name, weight=weight)

        pos = nx.spring_layout(G_nx)
        nx.draw(G_nx, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10)
        
        edge_labels = nx.get_edge_attributes(G_nx, 'weight')
        nx.draw_networkx_edge_labels(G_nx, pos, edge_labels=edge_labels)

        plt.show()


if __name__ == '__main__':
    graph = Graph('graph.csv')