from HashTable_dsa import HashEntry, HashTable
from DoubleLinkedList_dsa import DoubleLinkedList
from Queue_dll_dsa import Queue
from Stack_dll_dsa import Stack
'''
for each vertex store a list of the adjacent paths (vertices or edges)

'''

class Graph:
    # Makes a doubly linked list of vertexes and tracks the counts of edges and vertices
    def __init__(self):
        self.vertices_list = DoubleLinkedList()
        self.vertices_hashed = HashTable(100)
        self.vert_count = 0
        self.edge_count = 0

    # For test harness
    def vert_list(self):
        return self.vertices_list

    # Adds a vertex with just a name to the classes vertices list variable
    # Inserts last to iterate in added order later
    def add_vertex(self, name, data=None):
        if self.has_vertex(name) != True:
            vertex = Vertex(name, data)
            self.vertices_list.insert_last(vertex)
            self.vertices_hashed.insert(name, vertex)
            self.vert_count += 1
        else:
            print("Error: name already exists.")

    # Only adds an edge to existing vertices
    def add_edge(self, from_name, to_name):
        if self.has_vertex(from_name) == True and self.has_vertex(to_name) == True:
            from_vert = self.get_vertex(from_name)
            to_vert = self.get_vertex(to_name)
            edge = Edge(to_vert.name, to_vert)
            from_vert.links.insert_last(edge)
            self.edge_count += 1
        else:
            print("One or both names do not exist.")

    # Bool to check existence of vertex
    def has_vertex(self, name):
        has_name = self.vertices_hashed.retrieve(name)
        if has_name != None:
            return True
        else:
            return False

    # Int with O(1)
    def get_vertex_count(self):
        return self.vert_count

    # Int with O(1)
    def get_edge_count(self):
        return self.edge_count

    # Returns the node of a name
    def get_vertex(self, name):
        if self.has_vertex(name):
            return self.vertices_hashed.retrieve(name)
        else:
            print("Vertex not found")
            return None

    # Returns a doubly linked list of adjacents
    def get_adjacent(self, name):
        vert = self.get_vertex(name)
        return vert.links

    # Bool
    def points_to(self, from_name, to_name):
        adjacent = False
        if self.has_vertex(from_name) == True and self.has_vertex(to_name) == True:
            adj_list = self.get_adjacent(from_name)
            for edge in adj_list:
                if edge.direction == to_name:
                    adjacent = True
        else:
            print("One or both names not found")
        return adjacent

    # Returns void, prints to command line a formatted adjacency list
    def display_as_list(self):
        for vertex in self.vertices_list:
            string = vertex.name + ": ["
            for edge in vertex.links:
                string = string + edge.direction + ", "
            string = string[:-2]
            string = string + "]"
            print(string)

    # Visiting each of a vertices nodes before continuing, returns a doubly linked list of vertices
    # to iterate through for a display
    def bfsearch(self, start):
        self._clear()
        bfs_tree = DoubleLinkedList()
        q = Queue()
        bfs_tree.insert_last(start)
        start_vert = self.get_vertex(start)
        start_vert.visited = True
        q.enqueue(start_vert)

        while q.peek() != None:
            vert = q.dequeue()
            for edge in vert.links:
                curr_vert = self.get_vertex(edge.direction)
                if curr_vert.visited == False:
                    bfs_tree.insert_last(curr_vert.name)
                    curr_vert.visited = True
                    q.enqueue(curr_vert)

        return bfs_tree

    # Following the adjacent vertex path to a new node until none next
    def dfsearch(self, start):
        self._clear()
        dfs_tree = DoubleLinkedList()
        s = Stack()
        start_vert = self.get_vertex(start)
        start_vert.visited = True
        s.push(start_vert)

        while s.top() != None:
            vert = s.pull()
            dfs_tree.insert_last(vert.name)
            for edge in vert.links:
                new_vert = self.get_vertex(edge.direction)
                if new_vert.visited == False:
                    s.push(new_vert)
                    new_vert.visited = True
        return dfs_tree
            
    # Resetting the visited bool for for correct bfs and dfs
    def _clear(self):
        for i in self.vertices_list:
            i.visited = False

class Vertex:
    # Name is the searchable value, can contain data with data variable
    def __init__(self, name, data=None):
        self.name = name
        self.data = data
        self.links = DoubleLinkedList()
        self.visited = False

    def get_name(self):
        return self.name

    def get_value(self):
        return self.data

    def get_adjacent(self):
        return self.links


    def add_edge(self, edge):
        self.links.insert_last(edge)


class Edge:
    def __init__(self, direction, weight):
        self.direction = direction
        self.weight = weight


if __name__ == "__main__":
    
    # Printing out names of vertices in graph list
    g = Graph()
    g.add_vertex("A", "first alphabet letter")
    g.add_vertex("B", "second alphabet letter")
    g.add_vertex("C", "third alphabet letter")

    dll = g.vert_list()
    print("Looping through graph linked list of vertices:")
    for i in dll:
        print(i.name)
    print()

    # Getting vertex test
    print("getting vertex A: ", g.get_vertex("A").name)
    print()

    # Setting edge test
    print("Edge addition test\nEdge count before: ", g.get_edge_count())
    g.add_edge("A", "B")
    print("Edge count after: ", g.get_edge_count())

    # Testing getting adjacents to vertex
    print("Test for adjacents to A")
    g.add_edge("A", "C")
    print("Should be B and C:")
    adjacents = g.get_adjacent("A")
    for edge in adjacents:
        print(edge.direction)

    # Testing adjacent boolean
    print("\nTest for adjacent check between two vertices")
    print("Should return false: ", g.points_to("B", "C"))
    print("Should return true: ", g.points_to("A", "C"))

    # Testing display as list
    print("\nTest for display graph as adjacency list:")
    g.display_as_list()
    correct_format = "\nA: [B, C]\nB: [A]\nC: [A]"
    print("Compared to correct format:", correct_format)

    print("\nBreadth first search testing:")
    bfs = g.bfsearch("A")

    for i in bfs:
        print(i)

    # Testing depth first search function
    print("\nDepth first search testing:")
    dfs = g.dfsearch("A")

    for i in dfs:
        print(i)

    g.add_vertex("D", "riguhawe")    
    g.add_vertex("E", "warjhgnoj")    
    g.add_vertex("F", "OUWagohw")    

    g.add_edge("D", "E")
    g.add_edge("D", "F")
    g.add_edge("D", "A")
    g.add_edge("F", "B")
    print("\nFinal display test after adding 4 more edges:")
    g.display_as_list()
