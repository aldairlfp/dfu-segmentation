from random import randint
from math import log
import os 

class Min_Cut():
    def __init__(self, graph_file):
        # Load graph file
        self.graph = {}
        self.edges = 0
        self.vertex_count = 0
        with open(graph_file, "r") as file:
            for path in file:
                numbers = [int(x) for x in path.split() if x!='\n']
                vertex = numbers[0]
                vertex_edges = numbers[1:]
                self.graph[vertex] = vertex_edges
                self.edges+=len(vertex_edges)
                self.vertex_count+=1            
        self.supervertices = {}
        for key in self.graph:
            self.supervertices[key] = [key]
            
    # We  search the minimum cut
    def search_min_cut(self):
        minimumcut = 0
        while len(self.graph)>2:
            # Now we  Pick a random edge
            vertice1, vertice2 = self.select_random_edge()
            self.edges -= len(self.graph[vertice1])
            self.edges -= len(self.graph[vertice2])
            # Then we  merge the edges
            self.graph[vertice1].extend(self.graph[vertice2])
            # Update every references from v2 to point to v1
            for vertex in self.graph[vertice2]:
                self.graph[vertex].remove(vertice2)
                self.graph[vertex].append(vertice1)
            # Remove the  self loop
            self.graph[vertice1] = [x for x in self.graph[vertice1] if x != vertice1]
            # Update total edges of graph
            self.edges += len(self.graph[vertice1])
            self.graph.pop(vertice2)
            #  Update cut grouping in the graph
            self.supervertices[vertice1].extend(self.supervertices.pop(vertice2))
        #  we now Calculate the minimum cut
        for edges in self.graph.values():
            minimumcut = len(edges)
        #  finally return min cut and the two supervertices
        return minimumcut,self.supervertices      
        
    # select a  random edge:
    def select_random_edge(self):
        rand_edge = randint(0, self.edges-1)
        for vertex, vertex_edges in self.graph.items():
            if len(vertex_edges) < rand_edge:
                rand_edge -= len(vertex_edges)
            else:
                from_vertex = vertex
                to_vertex = vertex_edges[rand_edge-1]
                return from_vertex, to_vertex
                
    # Now we plot our graph
    def print_graph(self):
        for clue in self.graph:
            print("{} :{}".format(clue, self.graph[clue]))


if __name__ == "__main__":
    path_to_file = os.path.join( os.path.dirname(__file__), "data.txt")
    graph = Min_Cut(path_to_file)
    
    def wholekarger(iterations):
        graph = Min_Cut(path_to_file)
        output = graph.search_min_cut()
        minimumcut = output[0]
        supervertices = output[1]
    
        for i in range(iterations):
            graph = Min_Cut(path_to_file)
            output = graph.search_min_cut()
            if output[0] < minimumcut:
                minimumcut = output[0]
                supervertices = output[1]
        return minimumcut, supervertices
    
    output = wholekarger(10)
    print("minimumcut: {}\nsupervertices: {}".format(output[0],output[1]))