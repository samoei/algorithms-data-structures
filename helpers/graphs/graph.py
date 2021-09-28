class Graph:
    def __init__(self, num_nodes, edges) -> None:
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2  in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def __repr__(self) -> str:
        return "\n".join([f"{n} -> {neighbours}" for n, neighbours in enumerate(self.data)])
    def __str__(self) -> str:
        return self.__repr__()

def main():
    num_nodes = 5
    edges = [(0,1), (0,4), (1,4), (1,2), (2,3), (3,4)]
    g = Graph(num_nodes, edges)
    print(g)

if __name__ == "__main__":
    main()
