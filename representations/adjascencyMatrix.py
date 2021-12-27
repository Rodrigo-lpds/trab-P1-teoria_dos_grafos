#Adjascency Matrix representation in Python
class AdjMatrix:
    def __init__(self, num, graph):
        self.V = num
        self.graph = graph       

    
    def adjacency_matrix(self):
        """
        Returns the adjacency matrix of the graph.
        """
        adj_matrix = []
        unique_values = set()
        # get the unique values of the graph
        for line in self.graph:
            adj_matrix.append(line.split())
            unique_values.update(adj_matrix[-1])
        unique_values = list(unique_values)
        unique_values.sort()

        # create the adjacency matrix
        adj_matrix = [[0 for i in range(len(unique_values))] for j in range(len(unique_values))]
        for line in self.graph[1:]:
                adj_matrix[unique_values.index(line[0])][unique_values.index(line[2])] = 1
                adj_matrix[unique_values.index(line[2])][unique_values.index(line[0])] = 1
        return adj_matrix
    
    def print_agraph(self):
        # Print the graph
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in self.adjacency_matrix()]))