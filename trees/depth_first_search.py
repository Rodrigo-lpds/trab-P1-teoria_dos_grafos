class depth_first_search:
    def __init__(self, graph, start_vertex):
        self.graph = graph
        self.start_vertex = start_vertex
        self.visited = []
        self.stack = []
        self.stack.append(self.start_vertex)
        self.visited.append(self.start_vertex)
    
    def dfs(self):
        """
        Returns the depth first search of the graph.
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

        # create the visited list
        visited = [False for i in range(len(unique_values))]
        visited[unique_values.index(self.start_vertex)] = True

        # create the path list
        path = [None for i in range(len(unique_values))]

        # create the path list
        path[unique_values.index(self.start_vertex)] = self.start_vertex

        # create the result list
        result = []

        # while the stack is not empty
        while len(self.stack) > 0:
            # get the first element of the stack
            vertex = self.stack.pop()
            # for each vertex in the adjacency vector
            for i in adj_vector[unique_values.index(vertex)]:
                # if the vertex is not visited
                if not visited[unique_values.index(i)]:
                    # add the vertex to the stack
                    self.stack.append(i)
                    # add the vertex to the path
                    path[unique_values.index(i)] = vertex
                    # add the vertex to the visited list
                    visited[unique_values.index(i)] = True
                    # add the vertex to the result list
                    result.append(i)
        return result

    def print_result(self):
        """
        Prints the result of the depth first search.
        """
        print("Depth first search:")
        for i in self.dfs():
            print(i, end=" ")
        print()