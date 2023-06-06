class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, vortex1, vortex2):
        if vortex1 in self.adj_list.keys() and vortex2 in self.adj_list.keys():
            self.adj_list[vortex1].append(vortex2)
            self.adj_list[vortex2].append(vortex1)
            return True
        return False


my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1, 2)

my_graph.print_graph()

"""
    EXPECTED OUTPUT:
    ----------------
    1 : [2]
    2 : [1]

"""
