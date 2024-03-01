from utils import Graph, Node


graph = Graph(
    '/Users/danielcm585/Developer/data-mining/assignment/assignment05/graph.csv',
    is_directed=True
)

dist = graph.get_shortest_path('Farhan')
print(f"{'Node':10} {'Shortest Path':16}")
for i in range(len(graph.nodes)):
    node = graph.nodes[i]
    print("{:10} {:<16}".format(
        node.name,
        dist[node.id] if dist[node.id] < Graph.INFINITY else "-",
    ))
    