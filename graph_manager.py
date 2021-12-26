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
    
def breadth_first_search(graph, start_vertex):
    """
    Returns the breadth first search of the graph.
    """
    # get the unique values of the graph
    unique_values = set()
    for line in graph:
        unique_values.update(line.split())
    unique_values = list(unique_values)
    unique_values.sort()

    # create the adjacency vector
    adj_vector = [[] for i in range(len(unique_values))]
    for line in graph[1:]:
            adj_vector[unique_values.index(line[0])].append(line[2])
            adj_vector[unique_values.index(line[2])].append(line[0])

    # create the queue
    queue = []
    queue.append(start_vertex)

    # create the visited list
    visited = [False for i in range(len(unique_values))]
    visited[unique_values.index(start_vertex)] = True

    # create the path list
    path = [None for i in range(len(unique_values))]

    # create the path list
    path[unique_values.index(start_vertex)] = start_vertex

    # create the result list
    result = []

    # while the queue is not empty
    while len(queue) > 0:
        # get the first element of the queue
        vertex = queue.pop(0)
        # for each vertex in the adjacency vector
        for i in adj_vector[unique_values.index(vertex)]:
            # if the vertex is not visited
            if not visited[unique_values.index(i)]:
                # add the vertex to the queue
                queue.append(i)
                # add the vertex to the path
                path[unique_values.index(i)] = vertex
                # add the vertex to the visited list
                visited[unique_values.index(i)] = True
                # add the vertex to the result list
                result.append(i)
    return result

def depth_first_search(graph, start_vertex):
    """
    Returns the depth first search of the graph.
    """
    # get the unique values of the graph
    unique_values = set()
    for line in graph:
        unique_values.update(line.split())
    unique_values = list(unique_values)
    unique_values.sort()

    # create the adjacency vector
    adj_vector = [[] for i in range(len(unique_values))]
    for line in graph[1:]:
            adj_vector[unique_values.index(line[0])].append(line[2])
            adj_vector[unique_values.index(line[2])].append(line[0])

    # create the visited list
    visited = [False for i in range(len(unique_values))]
    visited[unique_values.index(start_vertex)] = True

    # create the path list
    path = [None for i in range(len(unique_values))]

    # create the path list
    path[unique_values.index(start_vertex)] = start_vertex

    # create the result list
    result = []

    # while the queue is not empty
    stack = []
    stack.append(start_vertex)
    while len(stack) > 0:
        # get the first element of the queue
        vertex = stack.pop()
        # for each vertex in the adjacency vector
        for i in adj_vector[unique_values.index(vertex)]:
            # if the vertex is not visited
            if not visited[unique_values.index(i)]:
                # add the vertex to the queue
                stack.append(i)
                # add the vertex to the path
                path[unique_values.index(i)] = vertex
                # add the vertex to the visited list
                visited[unique_values.index(i)] = True
                # add the vertex to the result list
                result.append(i)
    return result


#breadth_first_search_tree


#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
#     for row in adjacency_list(graph)]))
#print(adjacency_list(graph)[0])     
#print(breadth_first_search(graph, '3'))
#print(depth_first_search(graph, '3'))
