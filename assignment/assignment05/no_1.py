from utils import Graph, Node


graph = Graph('/Users/danielcm585/Developer/data-mining/assignment/assignment05/graph.csv')

print(f"{'Node':10} {'Degree Centrality':20} {'Neighbors':100}")
for i in range(len(graph.nodes)):
    node = graph.nodes[i]
    print("{:10} {:<20} {:100}".format(
        node.name,
        node.degree,
        ', '.join([
            f"{neighbor.name}({graph.adjacency_matrix[node.id][neighbor.id]})"
            for neighbor in node.neighbors
        ])
    ))
    