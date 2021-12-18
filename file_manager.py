def read_graph_file(file_name):
    """
    Reads a graph file and returns a list of all the lines in the file.
    """
    with open(file_name, 'r') as file:
        return file.readlines()

def get_vertex_quantity(graph): 
    """
    Returns the vertex of the graph.
    """
    return graph[0].rstrip("\n")

def get_edge_quantity(graph):
    """
    Returns the edge of the graph.
    """
    return len(graph) - 1	