class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edges(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def print_graph(self):
        for vertex, edges in self.adj_list.items():
            print(f"{vertex}: {', '.join(edges)}")

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            if self.adj_list.get(v1) and self.adj_list.get(v2):
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                return True
        return False

    def remove_vertex(self, vertex_name):
        if vertex_name in self.adj_list:
            vertex_to_remove = self.adj_list[vertex_name]
            for vertex in vertex_to_remove:
                self.adj_list[vertex].remove(vertex_name)
            del self.adj_list[vertex_name]
            return True
        return False


