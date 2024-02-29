from utils import Graph, Node


graph = Graph('/Users/danielcm585/Developer/data-mining/assignment/assignment05/graph.csv')

degree_centrality = graph.get_degree_centrality()
print(f"{'Node':10} {'Degree':8} {'Degree Centrality':20} {'Neighbors':100}")
for i in range(len(graph.nodes)):
    node = graph.nodes[i]
    print("{:10} {:<8} {:<20} {:100}".format(
        node.name,
        node.degree,
        degree_centrality[node.id],
        ', '.join([
            f"{neighbor.name}({graph.adjacency_matrix[node.id][neighbor.id]})"
            for neighbor in node.neighbors
        ])
    ))
    