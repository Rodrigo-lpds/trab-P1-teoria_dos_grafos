def read_graph_file(file_name):
    """
    Reads a graph file and returns a list of all the lines in the file.
    """
    with open(file_name, 'r') as file:
        return file.read().splitlines()