import file_manager as fm
import  graph_manager as gm

from representations.adjascencyList import AdjList
from representations.adjascencyMatrix import AdjMatrix
from representations.adjascencyVector import AdjVector

from trees.breadth_first_search import breadth_first_search
from trees.depth_first_search import depth_first_search

if __name__ == "__main__":
    graph_example = fm.read_graph_file('cases/grafo_1.txt')
    V = int(gm.get_vertex_quantity(graph_example))
    # Create graph and edges
    graph = AdjVector(V)
    #graph.adjacency_vector(graph_example)
    #graph.print_agraph(graph_example)
    tree_bfs = breadth_first_search(graph_example, '1')
    #tree_bfs.bfs()
    #tree_bfs.write_tree()
    #print(tree_bfs.get_distance('54'))

    tree_dfs = depth_first_search(graph_example, '1')
    tree_dfs.dfs()
    tree_dfs.write_tree()
    #print(tree_dfs.get_distance('5'))
    #spanning_tree = spanning_tree(graph_example, '1')
    #print(spanning_tree.get_tree())
