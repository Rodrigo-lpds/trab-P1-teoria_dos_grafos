import file_manager as fm

graph = fm.read_graph_file('graph_example.txt')


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
        if line[0] != '#':
            adj_matrix[unique_values.index(line[0])][unique_values.index(line[2])] = 1
            adj_matrix[unique_values.index(line[2])][unique_values.index(line[0])] = 1
    return adj_matrix

def adjacency_list(graph):
    """
    Returns the adjacency list of the graph.
    """
    adj_list = []
    unique_values = set()
    # get the unique values of the graph
    for line in graph:
        adj_list.append(line.split())
        unique_values.update(adj_list[-1])
    unique_values = list(unique_values)
    unique_values.sort()

    # create the adjacency list
    adj_list = [[] for i in range(len(unique_values))]
    for line in graph[1:]:
        if line[0] != '#':
            adj_list[unique_values.index(line[0])].append(line[2])
            adj_list[unique_values.index(line[2])].append(line[0])
    return adj_list


print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in adjacency_list(graph)]))
