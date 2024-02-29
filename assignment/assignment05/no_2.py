from utils import Graph, Node


graph = Graph(
    '/Users/danielcm585/Developer/data-mining/assignment/assignment05/graph.csv',
    is_directed=True
)
    
in_degree_centrality, out_degree_centrality = graph.get_degree_centrality()
print(f"{'Node':10} {'In Degree':12} {'Out Degree':12} {'In Degree Centrality':22} {'Out Degree Centrality':22}")
for i in range(len(graph.nodes)):
    node = graph.nodes[i]
    print("{:10} {:<12} {:<12} {:<22} {:<22}".format(
        node.name,
        node.in_degree,
        node.out_degree,
        in_degree_centrality[node.id],
        out_degree_centrality[node.id],
    ))
    