import file_manager as fm
import  graph_manager as gm

from representations.adjascencyList import AdjList
from representations.adjascencyMatrix import AdjMatrix
from representations.adjascencyVector import AdjVector

if __name__ == "__main__":
    graph_example = fm.read_graph_file('graph_example.txt')
    V = int(gm.get_vertex_quantity(graph_example))
    # Create graph and edges
    graph = AdjVector(V)
    #graph.adjacency_vector(graph_example)
    graph.print_agraph(graph_example)