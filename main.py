import math
import random

import file_manager as fm
import  graph_manager as gm

from representations.adjascencyList import AdjList
from representations.adjascencyMatrix import AdjMatrix
from representations.adjascencyVector import AdjVector

from trees.breadth_first_search import breadth_first_search
from trees.depth_first_search import depth_first_search

def estimate_diameter(graph,vertex_quantity):
        """
        Estimate the diameter of a graph.
        """
        diameter = 0
        k = math.log(vertex_quantity,2)
        k = math.pow(k,2)
        for i in range(int(k)):
            random_vertex = random.randint(1,vertex_quantity)
            tree_bfs = breadth_first_search(graph, str(random_vertex))
            tree_bfs.bfs()
            max_distance = tree_bfs.get_max_distance()
            if max_distance > diameter:
                diameter = max_distance
        return diameter
        
if __name__ == "__main__":
    graph_example = fm.read_graph_file('cases/grafo_1.txt')
    V = int(gm.get_vertex_quantity(graph_example))
    #tree_bfs = breadth_first_search(graph_example, '61')
    #tree_bfs.bfs()
    #print(tree_bfs.get_max_distance())
    print(estimate_diameter(graph_example,V))
    #tree_bfs.write_tree()
    #print(tree_bfs.get_distance('1'))

    #tree_dfs = depth_first_search(graph_example, '1')
    #tree_dfs.dfs()
    #print(tree_dfs.get_distance('5'))
    #spanning_tree = spanning_tree(graph_example, '1')
    #print(spanning_tree.get_tree())

    