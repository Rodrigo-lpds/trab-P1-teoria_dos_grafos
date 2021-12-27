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
 