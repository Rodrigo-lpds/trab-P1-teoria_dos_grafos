import math
import random

from trees.breadth_first_search import breadth_first_search

def get_vertex_quantity(graph): 
    """
    Returns the vertex of the graph.
    """
    return int(graph[0].rstrip("\n"))

def get_edge_quantity(graph):
    """
    Returns the edge of the graph.
    """
    return len(graph) - 1	

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
