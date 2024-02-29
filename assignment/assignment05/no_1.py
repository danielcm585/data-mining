from utils import Graph, Node


graph = Graph('/Users/danielcm585/Developer/data-mining/assignment/assignment05/graph.csv')

degree_centrality = graph.get_degree_centrality()
for i in range(len(graph.nodes)):
    node = graph.nodes[i]
    print(node)
    print(f"> degree centrality: {degree_centrality[node.id]}")
    print(f"> neighbors:")
    for neighbor in node.neighbors:
        print(f"  - {neighbor} ({graph.adjacency_matrix[node.id][neighbor.id]})")
    