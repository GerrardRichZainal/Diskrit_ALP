import networkx as nx
import matplotlib.pyplot as plt

class Graf:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph = nx.DiGraph() if directed else nx.Graph()

    # =================================================
    # METODE DASAR 
    # =================================================
    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, u, v, weight=1):
        self.graph.add_edge(u, v, weight=weight)

    def visualize_graph(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(
            self.graph, pos,
            with_labels=True,
            node_size=2500,
            node_color="skyblue"
        )
        labels = nx.get_edge_attributes(self.graph, "weight")
        nx.draw_networkx_edge_labels(
            self.graph, pos, edge_labels=labels
        )
        plt.show()

    def shortest_path(self, source, target):
        return nx.shortest_path(
            self.graph,
            source=source,
            target=target,
            weight="weight"
        )

    def visual_shortest_path(self, source, target):
        path = self.shortest_path(source, target)
        pos = nx.spring_layout(self.graph)

        nx.draw(
            self.graph, pos,
            with_labels=True,
            node_size=2500,
            node_color="lightgray"
        )

        edges = list(zip(path, path[1:]))

        nx.draw_networkx_nodes(
            self.graph, pos,
            nodelist=path,
            node_color="orange"
        )
        nx.draw_networkx_edges(
            self.graph, pos,
            edgelist=edges,
            width=3,
            edge_color="red"
        )

        labels = nx.get_edge_attributes(self.graph, "weight")
        nx.draw_networkx_edge_labels(
            self.graph, pos, edge_labels=labels
        )
        plt.show()

    # =================================================
    # METODE TAMBAHAN
    # =================================================
    def node_degree(self):
        return dict(self.graph.degree())

    def is_connected(self):
        if self.directed:
            return nx.is_strongly_connected(self.graph)
        return nx.is_connected(self.graph)

    def find_cycles(self):
        if self.directed:
            return list(nx.simple_cycles(self.graph))
        return nx.cycle_basis(self.graph)

    def bfs(self, start):
        return list(nx.bfs_tree(self.graph, start))

    def dfs(self, start):
        return list(nx.dfs_preorder_nodes(self.graph, start))

    def dijkstra(self, start):
        return nx.single_source_dijkstra_path_length(self.graph, start)

    def has_path(self, source, target):
        return nx.has_path(self.graph, source, target)

    def graph_info(self):
        return {
            "Jumlah Node": self.graph.number_of_nodes(),
            "Jumlah Edge": self.graph.number_of_edges(),
            "Directed": self.directed
        }
