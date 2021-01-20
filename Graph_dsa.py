from HashTable_dsa import HashEntry, HashTable
from DoubleLinkedList_dsa import DoubleLinkedList
from Queue_dll_dsa import Queue
from Stack_dll_dsa import Stack
import numpy as np


class Graph:
    """
    Data Structure written and previously submitted, used for traversals of
    trading data
    """
    def __init__(self):
        """Graph object has a doubly linked list of vertexes,
            tracks the counts of edges and vertices,
            and has a hash table of vertices for 0(1) operations"""
        self.vertices_list = DoubleLinkedList()
        self.vertices_hashed = HashTable(100)
        self.vert_count = 0
        self.edge_count = 0

    def vert_list(self):
        """Returns the doubly linked list of vertices"""
        return self.vertices_list

    def add_vertex(self, name, data=None):
        """Adds a vertex with just a name to the classes vertices list variable
            inserts last to iterate in added order later."""
        if self.has_vertex(name) != True:
            vertex = Vertex(name, data)
            self.vertices_list.insert_last(vertex)
            self.vertices_hashed.insert(name, vertex)
            self.vert_count += 1
        else:
            print("Error: name already exists.")

    def add_edge(self, from_name, to_name, data):
        """Only adds an edge to existing vertices."""
        if self.has_vertex(from_name) == True and self.has_vertex(to_name) == True:
            from_vert = self.get_vertex(from_name)
            to_vert = self.get_vertex(to_name)
            edge = Edge(from_name, to_name, data)
            from_vert.links.insert_last(edge)
            self.edge_count += 1
        else:
            print("One or both names do not exist.")

    def has_vertex(self, name):
        """Returns bool checking whether name exists as a vertex in Graph."""
        has_name = self.vertices_hashed.retrieve(name)
        if has_name != None:
            return True
        else:
            return False

    def get_vertex_count(self):
        """Returns integer of how many vertices are in the graph."""
        return self.vert_count

    def get_edge_count(self):
        """Returns integer of how many edges are in the graph."""
        return self.edge_count

    def get_vertex(self, name):
        """Returns a Vertex in O(1) through a hash table retrieve,
            if not found will return None."""
        if self.has_vertex(name):
            return self.vertices_hashed.retrieve(name)
        else:
            print("Vertex not found")
            return None

    def get_adjacent(self, name):
        """Return a Linked List of the arcs of a symbol entered in O(1)."""
        vert = self.get_vertex(name)
        return vert.links

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

    def display_as_list(self):
        """Returns void, prints to command line a formatted adjacency list."""
        for vertex in self.vertices_list:
            string = vertex.name + ": ["
            for edge in vertex.links:
                string = string + edge.end + ", "
            string = string[:-2]
            string = string + "]"
            print(string)

    def display_edges(self, vertex_name):
        """Gets vertex from symbol and prints to command line
            the adjacent vertices."""
        vertex = self.vertices_hashed.retrieve(vertex_name)
        edge_str = vertex_name +  ": "
        for edge in vertex.links:
            edge_str = edge_str + edge.end + " "
        print(edge_str)

    def bfs_shortest_path(self, start, end):
        """Finds the shortest path from one Vertex to another
            regardless of edge weight through a depth first search
            returning None if not found."""
        visited = DoubleLinkedList()
        queue = Queue()
        throw_away = DoubleLinkedList()
        throw_away.insert_last(start)
        queue.enqueue(throw_away)

        while queue.count() > 0:
            path = queue.dequeue()
            vert_name = path.peek_last()

            if vert_name == end:
                return path

            if visited.has(vert_name) == False:
                edge_list = self.get_adjacent(vert_name)
                for current_edge in edge_list:
                    new_path = path.copy_list()
                    new_path.insert_last(current_edge.end)
                    queue.enqueue(new_path)

                visited.insert_last(vert_name)
        print("Path does not exist")
        return None

    def dfs_shortest_path(self, start, stop):
        '''Following the path that maximises profit by arcs in a depth first search traversal
            returning None if one could not be found.'''
        total_weight = 0
        found = False
        self.clear()
        path = DoubleLinkedList()
        parent_map = HashTable(10)

        q = Queue()
        start_vert = self.get_vertex(start)
        start_vert.visited = True
        q.enqueue(start_vert)

        while q.peek() != None:
            if found:
                break
            vert = q.dequeue()

            min_to_max_edges = self.sort_edge_weight(vert.links)
            for i in range(len(min_to_max_edges)):
                curr_vert = self.get_vertex(min_to_max_edges[i].end)
                if curr_vert.visited == False:
                    if curr_vert.name == stop:
                        parent_map.insert(curr_vert.name, PathNode(vert.name, float(min_to_max_edges[i].weight)))
                        key = curr_vert.name
                        while (key != None):
                            path.insert_last(key)
                            key = parent_map.retrieve(key)
                            if key != None:
                                total_weight = total_weight + key.cost
                                key = key.point
                        found = True
                        break
                    q.enqueue(curr_vert) 
                    parent_map.insert(curr_vert.name, PathNode(vert.name, float(min_to_max_edges[i].weight)))
                    curr_vert.visited = True
        if not found:
            print(start, "to ", stop, "could not be found")
            return None
        else:
            print("\nTOTAL WEIGHTED AVERAGE PRICE: ", round(total_weight, 2), "\n")
            return path.reverse()

    def old_dfs(self, start, stop):
        '''Following the path that maximises profit by arcs in a depth first search traversal
            returning None if one could not be found.'''
        total_weight = 0
        found = False
        self.clear()
        parents = DoubleLinkedList()

        s = Stack()
        start_vert = self.get_vertex(start)
        start_vert.visited = True
        s.push(start_vert)

        while s.top() != None:
            if found:
                break
            vert = s.pull()

            min_to_max_edges = self.sort_edge_weight(vert.links)
            for i in range(len(min_to_max_edges)):
                curr_vert = self.get_vertex(min_to_max_edges[i].end)
                if curr_vert.visited == False:
                    if curr_vert.name == stop:
                        found = True
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
            print()
            print("TOTAL WEIGHTED AVERAGE PRICE: ", round(total_weight, 2))
            print()
            return parents

    def clear(self):
        """Resets all vertex visited variables to false before a traversal,
            done in O(n)."""
        for i in self.vertices_list:
            i.visited = False

    def sort_edge_weight(self, list_to_sort):
        """Returns an array sorted by edges."""
        arcs_sorting = self.linked_list_to_array_edges(list_to_sort)
        for i in range(1, len(arcs_sorting)):
            key = arcs_sorting[i]
            j = i-1
            while j >=0 and float(key.weight) > float(arcs_sorting[j].weight):
                arcs_sorting[j+1] = arcs_sorting[j]
                j -= 1
            arcs_sorting[j+1] = key
        return arcs_sorting

    def linked_list_to_array_edges(self, linked_list):
        """Returns an array of the given linked list by iterating through
            the list and assigning each array index the same value"""
        size = linked_list.count
        array = np.zeros(size, dtype=object)
        index = 0
        for edge in linked_list:
            array[index] = edge
            index += 1
        return array

class Vertex:
    def __init__(self, name, data=None):
        """ Name is the searchable value, can contain data with data variable
            the arcs are in the linked list, and visited bool 
            prevents repeats in a traversal."""
        self.name = name
        self.data = data
        self.links = DoubleLinkedList()
        self.visited = False

    def get_name(self):
        """Method that returns the Vertex name."""
        return self.name

    def get_value(self):
        """Method that returns the data stored by the Vertex."""
        return self.data

    def get_adjacent(self):
        """method that returns the linked list of arcs."""
        return self.links


    def add_edge(self, edge):
        """Method that adds an edge to the linked list of arcs
            going from the Vertex.""" 
        self.links.insert_last(edge)


class Edge:
    def __init__(self, start, end, weight):
        """Edge object records where the Edge is coming from,
            going to, and its weight."""
        self.start = start
        self.end = end
        self.weight = weight

class PathNode:
    def __init__(self, point, cost):
        """Path object to contain traversal parents of child nodes
            and what it cost to go to them."""
        self.point = point
        self.cost = cost


