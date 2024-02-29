from utils import Graph, Node


graph = Graph('/Users/danielcm585/Developer/data-mining/assignment/assignment05/graph.csv')

degree_centrality = graph.get_degree_centrality()
for i in range(len(graph.nodes)):
    node = graph.nodes[i]
    print(f"{node}'s degree centrality is {degree_centrality[node.id]} and these are the neighbors:")
    for neighbor in node.neighbors:
        print(f"- {neighbor}")
    