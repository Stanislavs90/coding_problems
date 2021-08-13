#https://www.youtube.com/watch?v=wAlyAw1ikdQ


# adj_list = {
#     "A": ["B","C"],
#     "B": ["A","D","E"],
#     "C": ["A","D"],
#     "D": ["C","B","E"],
#     "E": ["B","D"]
# }

# print(adj_list["B"])

edges = []

class Graph:
    def __init__(self, Nodes):
        self.nodes = Nodes
        self.adj_list = {}

        # loop to create list
        for node in self.nodes:
            # vertex
            self.adj_list[node] = []

    def add_edge(self, vertex, edge):
        self.adj_list[vertex].append(edge)
        self.adj_list[edge].append(vertex)

    def print_adj(self):
        for node in self.nodes:
            print(node, ":", self.adj_list[node])
    

nodes = ["A", "B","C","D","E"]
graph = Graph(nodes)
graph.add_edge("A", "B")
graph.print_adj()