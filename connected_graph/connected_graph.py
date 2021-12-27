from trees.breadth_first_search import breadth_first_search

class connected_graph:
    def __init__(self,graph,vertex_quantity):
        self.graph = graph
        self.vertex_quantity = vertex_quantity
        self.connected_graphs = []

    def get_connected_graphs(self):
        """
        Returns a list of connected graphs.
        """
        #create vertext list
        vertex_list = [str(i) for i in range(1,self.vertex_quantity+1)]
        while len(vertex_list) > 0:
            tree_bfs = breadth_first_search(self.graph, vertex_list[0])
            identified_vertices = tree_bfs.bfs()
            #append the identified vertices to the connected graph list
            self.connected_graphs.append(identified_vertices)
            #remove vertex of teste in vertex_list
            vertex_list.remove(vertex_list[0])
            for vertex in identified_vertices:
                vertex_list.remove(vertex)
        self.connected_graphs = sorted(self.connected_graphs, key=len,reverse=True)
        
        return self.connected_graphs

    def print_connected_graphs(self):
        """
        Prints the connected graphs.
        """
        print('Connected graphs:')
        for i in range(len(self.connected_graphs)):
            print('Graph '+str(i+1)+':')
            print('Vertex quantity: '+str(len(self.connected_graphs[i])))
            print('Vertices: '+str(self.connected_graphs[i]))
            print('\n')