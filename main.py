import file_manager as fm
import  graph_manager as gm

from representations.adjascencyList import AdjList

if __name__ == "__main__":
    graph_example = fm.read_graph_file('graph_example.txt')
    V = int(gm.get_vertex_quantity(graph_example))
    # Create graph and edges
    graph = AdjList(V+1)
    for line in graph_example[1:]:
        line = line.split(' ')
        graph.add_edge(int(line[0]), int(line[1]))
    graph.print_agraph()