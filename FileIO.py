from Graph_dsa import Graph
from DoubleLinkedList_dsa import DoubleLinkedList

class GraphProcessor:

    def graph(self, file_name):
        # Reads the filename provided and calls a private method to process
        # into a graph the parsed data
        try:
            with open(file_name, "r") as reader:
                dll_a = DoubleLinkedList()
                dll_b = DoubleLinkedList()
                for line in reader.readlines():
                    dll_a.insert_last(line[0])
                    dll_b.insert_last(line[2])
            proc_graph = self._graph(dll_a, dll_b)
            return proc_graph
                
        except:
            print("Error: File not found.")

    # Takes two doubly linked lists of vertices each step having an edge    
    # Returns a Graph object
    def _graph(self, verts_a, verts_b):
        graph = Graph()
        for i, j in zip(verts_a, verts_b):
            if graph.has_vertex(i) == False:
                graph.add_vertex(i)
            if graph.has_vertex(j) == False:
                graph.add_vertex(j)
            graph.add_edge(i, j)
        return graph

if __name__ == "__main__":

    # Test Harness
    print("Testing read function input from file 1")
    processor = GraphProcessor()
    graph1 = processor.graph("prac6_1.al")
    graph1.display_as_list()
    print("\nTesting read function input from file 2")
    graph2 = processor.graph("prac6_2.al")
    graph2.display_as_list()

    
    # Breadth first search tests
    bfs = graph1.bfsearch("A")
    print("Breadth first search graph 1:")
    for i in bfs:
        print(i)
    
    bfs2 = graph2.bfsearch("A")
    print("Breadth first search graph 2:")
    for i in bfs2:
        print(i)
    
    # Depth first search tests
    dfs = graph1.dfsearch("A")
    print("\nDepth first search graph 1:")
    for i in dfs:
        print(i)

    dfs2 = graph2.dfsearch("A")
    print("\nDepth first search graph 2:")
    for i in dfs2:
        print(i)

    
