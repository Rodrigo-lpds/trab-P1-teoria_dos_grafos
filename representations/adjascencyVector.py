# Adjascency Vector representation in Python
class AdjVector:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    def adjacency_vector(self, graph):
        # get the unique values of the graph
        unique_values = set()
        for line in graph:
            unique_values.update(line.split())
        unique_values = list(unique_values)
        unique_values.sort()

        # create the adjacency vector
        adj_vector = [[] for i in range(len(unique_values))]
        for line in graph[1:]:
            line = line.split()
            adj_vector[unique_values.index(line[0])].append(line[1])
            adj_vector[unique_values.index(line[1])].append(line[0])
        return adj_vector

    def print_agraph(self, graph):    
        # Print the graph
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in self.adjacency_vector(graph)]))