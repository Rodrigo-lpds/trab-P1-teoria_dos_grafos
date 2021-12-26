#Adjascency Matrix representation in Python
class AdjMatrix:
    def __init__(self, num):
        self.V = num
        self.graph = [[0 for i in range(self.V)] for j in range(self.V)]

    # Add edges
    def add_edge(self, s, d):
        self.graph[s][d] = 1
        self.graph[d][s] = 1

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            for j in range(self.V):
                print(self.graph[i][j], end=" ")
            print("\n")