from utils import Graph, Node


graph = Graph(
    '/Users/danielcm585/Developer/data-mining/assignment/assignment05/graph.csv',
    is_directed=True
)

print(f"{'Node':10} {'In Degree Centrality':22} {'Out Degree Centrality':22}")
for i in range(len(graph.nodes)):
    node = graph.nodes[i]
    print("{:10} {:<22} {:<22}".format(
        node.name,
        node.in_degree,
        node.out_degree,
    ))
    