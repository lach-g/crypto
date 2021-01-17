from HashTable_dsa import HashEntry, HashTable
from DoubleLinkedList_dsa import DoubleLinkedList
from Queue_dll_dsa import Queue
from Stack_dll_dsa import Stack

import numpy as np
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
    def add_edge(self, from_name, to_name, data):
        if self.has_vertex(from_name) == True and self.has_vertex(to_name) == True:
            from_vert = self.get_vertex(from_name)
            to_vert = self.get_vertex(to_name)
            edge = Edge(from_name, to_name, data)
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
                if edge.end == to_name:
                    adjacent = True
        else:
            print("One or both names not found")
        return adjacent

    # Returns void, prints to command line a formatted adjacency list
    def display_as_list(self):
        for vertex in self.vertices_list:
            string = vertex.name + ": ["
            for edge in vertex.links:
                string = string + edge.end + ", "
            string = string[:-2]
            string = string + "]"
            print(string)

    def display_edges(self, vertex_name):
        vertex = self.vertices_hashed.retrieve(vertex_name)
        edge_str = vertex_name +  ": "
        for edge in vertex.links:
            edge_str = edge_str + edge.end + " "
        print(edge_str)

    # To reach a vertex by travelling across as few different arcs as possible
    def breadth_first_search_path(self, start, stop):
        # Setup
        path = DoubleLinkedList()
        found = False
        self._clear()
        q = Queue()
        start_vert = self.get_vertex(start)
        start_vert.visited = True
        q.enqueue(start_vert)

        # While vertices are remaining continue
        while q.peek() != None:

            if found:
                break

            # Iterate through vertex arcs
            vert = q.dequeue()
            for arc in vert.links:
                curr_vert = self.get_vertex(arc.end)

                # Only check matching and path for unvisited vertices
                if curr_vert.visited == False:
                    if curr_vert.name == stop:
                        found = True
                        if path.has(arc.start) == False:
                            path.insert_last(arc.end)
                        break
                    if path.has(arc.start) == False:
                        path.insert_last(arc.start)
                    curr_vert.visited = True
                    q.enqueue(curr_vert)
        if not found:
            print(start, "to ", stop, "could not be found")
            return None
        else:
            return path


    def bfs_shortest_path(self, start, end):
        visited = DoubleLinkedList()
        queue = Queue()
        throw_away = DoubleLinkedList()
        throw_away.insert_last(start)
        queue.enqueue(throw_away)

        while queue.count() > 0:
            # Gets first path in queue
            path = queue.dequeue()
            # Gets last node in path
            vert_name = path.peek_last()

            # Checks if node is end
            if vert_name == end:
                return path

            # Check if current node is visited to avoid rechecking
            if visited.has(vert_name) == False:
                print()
                print(vert_name)
                edge_list = self.get_adjacent(vert_name)
                # Go through adjacent vertices adding each as a potential path
                for current_edge in edge_list:
                    new_path = path.copy_list()
                    new_path.insert_last(current_edge.end)
                    print(new_path)
                    queue.enqueue(new_path)
                print()

                visited.insert_last(vert_name)
        print("Path does not exist")






    '''Following the path that maximises profit by arcs in a depth first search traversal'''
    def dfsearch(self, start, stop):
        total_weight = 0
        found = False
        self._clear()
        dfs_tree = DoubleLinkedList()

        parents = DoubleLinkedList()

        s = Stack()
        start_vert = self.get_vertex(start)
        start_vert.visited = True
        s.push(start_vert)

        while s.top() != None:
            if found:
                break
            vert = s.pull()

            # No dead ends added to list
            if vert.links != None:
                dfs_tree.insert_last(vert)

            min_to_max_edges = self.sort_edge_weight(vert.links)
            for i in range(len(min_to_max_edges)):
                curr_vert = self.get_vertex(min_to_max_edges[i].end)
                if curr_vert.visited == False:
                    print("From: ", min_to_max_edges[i].start, "\tTo: ", min_to_max_edges[i].end, "weight: ", min_to_max_edges[i].weight)
                    if curr_vert.name == stop:
                        found = True
                        dfs_tree.insert_last(curr_vert)
                        if parents.has(min_to_max_edges[i].start) == False:
                            parents.insert_last(min_to_max_edges[i].start)
                        parents.insert_last(min_to_max_edges[i].end)
                        total_weight += float(min_to_max_edges[i].weight)
                        break

                    if parents.has(min_to_max_edges[i].start) == False:
                        parents.insert_last(min_to_max_edges[i].start)
                        total_weight += float(min_to_max_edges[i].weight)

                    s.push(curr_vert)
                    curr_vert.visited = True
        if not found:
            print(start, "to ", stop, "could not be found")
            return None
        else:
            print("The parents sol:")
            for i in parents:
                print(i)
            print("TOTAL WEIGHT: ", total_weight)
            return dfs_tree



    # Resetting the visited bool for for correct bfs and dfs
    def _clear(self):
        for i in self.vertices_list:
            i.visited = False

    def sort_edge_weight(self, list_to_sort):
        A = self.linked_list_to_array_edges(list_to_sort)
        for i in range(1, len(A)):
            key = A[i]
            j = i-1
            while j >=0 and float(key.weight) > float(A[j].weight):
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key
        return A

    def linked_list_to_array_edges(self, linked_list):
        size = linked_list.count
        array = np.zeros(size, dtype=object)
        index = 0
        for edge in linked_list:
            array[index] = edge
            index += 1
        return array

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
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
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
        print(edge.end)

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
    dfs = g.old_dfsearch("A")

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
