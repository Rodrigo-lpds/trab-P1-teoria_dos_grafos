# Adjascency Vector representation in Python
class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


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
            adj_list[unique_values.index(line[0])].append(line[2])
            adj_list[unique_values.index(line[2])].append(line[0])
    return adj_list
