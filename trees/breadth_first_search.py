class breadth_first_search:
    def __init__(self, graph, start_vertex):
        self.graph = graph
        self.start_vertex = start_vertex
        self.visited = []
        self.queue = []
        self.queue.append(self.start_vertex)
        self.visited.append(self.start_vertex)
    
    def bfs(self):
        """
        Returns the breadth first search of the graph.
        """
        # get the unique values of the graph
        unique_values = set()
        for line in self.graph:
            unique_values.update(line.split())
        unique_values = list(unique_values)
        unique_values.sort()
        # create the adjacency vector
        adj_vector = [[] for i in range(len(unique_values))]
        for line in self.graph[1:]:
            line = line.split()
            adj_vector[unique_values.index(line[0])].append(line[1])
            adj_vector[unique_values.index(line[1])].append(line[0])

        # create the queue
        queue = []
        queue.append(self.start_vertex)

        # create the visited list
        visited = [False for i in range(len(unique_values))]
        visited[unique_values.index(self.start_vertex)] = True

        # create the path list
        path = [None for i in range(len(unique_values))]

        # create the path list
        path[unique_values.index(self.start_vertex)] = self.start_vertex

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
    
    def print_result(self):
        """
        Prints the breadth first search result.
        """
        print('Breadth first search result:')
        print(self.bfs())
        print()
