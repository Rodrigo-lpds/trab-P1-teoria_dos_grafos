import file_manager as fm
import  graph_manager as gm

from representations.adjascencyList import AdjList
from representations.adjascencyMatrix import AdjMatrix
from representations.adjascencyVector import AdjVector

from trees.breadth_first_search import breadth_first_search
from trees.depth_first_search import depth_first_search

from connected_graph.connected_graph import connected_graph


if __name__ == "__main__":
    graph_example = fm.read_graph_file('cases/grafo_2.txt')
    V = int(gm.get_vertex_quantity(graph_example))
    #tree_bfs = breadth_first_search(graph_example, '6')
    #tree_bfs.bfs()
    #tree_bfs.print_result()
    conn = connected_graph(graph_example, V)
    print(conn.get_connected_graphs())
    conn.print_connected_graphs()
    #print(tree_bfs.get_connected_graphs())

    #print graph to pdf

    #print(tree_bfs.get_max_distance())
    #print(estimate_diameter(graph_example,V))
    #tree_bfs.write_tree()
    #print(tree_bfs.get_distance('1'))

    #tree_dfs = depth_first_search(graph_example, '1')
    #tree_dfs.dfs()
    #print(tree_dfs.get_distance('5'))
    #spanning_tree = spanning_tree(graph_example, '1')
    #print(spanning_tree.get_tree())

    