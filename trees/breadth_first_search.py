class breadth_first_search:
    def __init__(self, graph, start_vertex):
        self.graph = graph
        self.start_vertex = start_vertex
        self.visited = []
        self.queue = []
        self.path = []
        self.distance = 1
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
        self.path = [None for i in range(len(unique_values))]
       
        # create the path list
        self.path[unique_values.index(self.start_vertex)] = self.start_vertex

        # create the result list
        result = []

        # while the queue is not empty
        while len(queue) > 0:
            #print(self.path)
            # get the first element of the queue
            vertex = queue.pop(0)
            # for each vertex in the adjacency vector
            for i in adj_vector[unique_values.index(vertex)]:
                # if the vertex is not visited
                if not visited[unique_values.index(i)]:
                    # add the vertex to the queue
                    queue.append(i)
                    # add the vertex to the path
                    self.path[unique_values.index(i)] = vertex
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
    
    def get_distance(self,vertex):
        """
        Returns distance between two nodes.
        """
        self.distance = 1
        parent = self.path[int(vertex)-1]
        if parent == self.start_vertex:
            return self.distance
        if int(parent) == int(vertex):
            return "No path"
        while (str(parent)!= self.start_vertex and int(parent) != int(vertex)):
            children = parent
            parent = self.path[int(parent)-1]
            if(children == parent or self.distance > len(self.path)):
                return "No path"
            self.distance += 1
        return self.distance
    
    def get_max_distance(self):
        
        """
        Returns the maximum distance from the start node.
        """
        max_distance = 0
        for node, parent in enumerate(self.path):
            
            if parent != None:
                distance = self.get_distance(node+1)
               
                if distance != "No path" and distance > max_distance:
                    max_distance = distance
        return max_distance
    
    def write_tree(self):
        """
        Writes the breadth first search result to a file.
        """
        with open('bfs_result.txt', 'w') as file:
            file.write('Breadth first spanning tree:')
            file.write('\n')
            file.write('Node | Parent | Distance from start node')
            file.write('\n')
            for node, parent in enumerate(self.path):
                if parent != None:
                    file.write(str(node+1)+' | '+str(parent)+ ' | '+ str(self.get_distance(node+1)) +'\n')
                print("Node: ", node+1, "Parent: ", parent)
        print('Breadth first spanning tree written to file.')
        print()
    
    def connected_graph(self):
        """
        Returns true if the graph is connected, false otherwise.
        """
        
        if len(self.bfs()) == int(self.graph[0].split()[0]) - 1:
            return True
        return False 
    
        