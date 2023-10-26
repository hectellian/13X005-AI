from assignment2.datastructures.node import Node

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation
from typing import List

class GraphVisualizer:
    def __init__(self, graph_edges):
        self.G = nx.DiGraph(graph_edges)  # Use DiGraph for directed graph
        self.pos = nx.spring_layout(self.G)

    def plot_graph(self):
        nx.draw(self.G, self.pos, with_labels=True, node_color='skyblue', node_size=1500, width=2.0, alpha=0.6, arrows=True)  # arrows=True to show direction


class SearchPathVisualizer(GraphVisualizer):
    def plot_search_path(self, path: List[Node]):
        """Visualize the graph with the search path."""
        super().plot_graph()  # Plot the base graph

        # Highlight the path edges in red
        path_edges = [(path[i].state, path[i+1].state) for i in range(len(path)-1)]
        nx.draw_networkx_edges(self.G, self.pos, edgelist=path_edges, edge_color='r', node_size=1500, width=3, arrows=True) 

        nx.draw_networkx_nodes(self.G, self.pos, nodelist='S', node_color='red', node_size=1500, alpha=0.6)
        nx.draw_networkx_nodes(self.G, self.pos, nodelist='G', node_color='green', node_size=1500, alpha=0.6)

        plt.show()
