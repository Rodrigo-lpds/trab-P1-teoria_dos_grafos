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

def adjacency_matrix(graph):
    """
    Returns the adjacency matrix of the graph.
    """
    adj_matrix = []
    unique_values = set()
    # get the unique values of the graph
    for line in graph:
        adj_matrix.append(line.split())
        unique_values.update(adj_matrix[-1])
    unique_values = list(unique_values)
    unique_values.sort()

    # create the adjacency matrix
    adj_matrix = [[0 for i in range(len(unique_values))] for j in range(len(unique_values))]
    for line in graph[1:]:
            adj_matrix[unique_values.index(line[0])][unique_values.index(line[2])] = 1
            adj_matrix[unique_values.index(line[2])][unique_values.index(line[0])] = 1
    return adj_matrix

# get the adjancency vector of the graph
def adjacency_vector(graph):
    """
    Returns the adjacency list of the graph.
    """
    adj_vector = []
    unique_values = set()
    # get the unique values of the graph
    for line in graph:
        adj_vector.append(line.split())
        unique_values.update(adj_vector[-1])
    unique_values = list(unique_values)
    unique_values.sort()

    # create the adjacency vector
    adj_vector = [[] for i in range(len(unique_values))]
    for line in graph[1:]:
            adj_vector[unique_values.index(line[0])].append(line[2])
            adj_vector[unique_values.index(line[2])].append(line[0])
    return adj_vector
    