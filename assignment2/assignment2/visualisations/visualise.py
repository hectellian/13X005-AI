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


class SearchAnimationVisualizer(GraphVisualizer):
    def animate_search(self, search_steps: List[Node]):
        fig, ax = plt.subplots(figsize=(10, 8))

        def update(num):
            ax.clear()

            GraphVisualizer.plot_graph(self) # Plot the base graph
            
            current_node = search_steps[num]
            visited_nodes = search_steps[:num+1]
            
            nx.draw_networkx_nodes(self.G, self.pos, nodelist='S', node_color='red', node_size=1500, alpha=0.6)
            nx.draw_networkx_nodes(self.G, self.pos, nodelist='G', node_color='green', node_size=1500, alpha=0.6)
            
            # If there's more than one visited node, highlight the edge between the last two visited nodes
            if len(visited_nodes) > 1:
                nx.draw_networkx_edges(self.G, self.pos, ax=ax, edgelist=[(visited_nodes[-2], visited_nodes[-1])], edge_color='red', width=2.0, arrows=True)

        ani = FuncAnimation(fig, update, frames=len(search_steps), repeat=False)
        plt.close(ani._fig)
        return ani
