"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):

        if(len(self.vertices[v1]) == 0):
            self.vertices[v1] = {v2}
        else:
            self.vertices[v1].add(v2)
        if(len(self.vertices[v2]) == 0):
            self.vertices[v2] = {v1}
        else:
            self.vertices[v2].add(v1)

            sorted(self.vertices[v1])
            sorted(self.vertices[v2])

    def bft(self, starting_vertex):
        # start with top node
        # see neighbor nodes 
        neighborNodesToVisit = Queue()
        visitedObj = {}
        visitedNodes = []
        
        # use queue to keep track of nodes that you need to visit. 
        for vertice in self.vertices[starting_vertex]:
            neighborNodesToVisit.enqueue(vertice)
        
        currentLayer = []

        while not neighborNodesToVisit.size == 0:
            node = neighborNodesToVisit.dequeue()

            # visit each node and keep track
            if not visitedObj[node]:
                visitedNodes.append(node)
                currentLayer.append(node)
                visitedObj[node] = True

            # after going through each neighbor nodes of the first layer         
            if neighborNodesToVisit.size == 0:
                 for vertice in currentLayer:
                    # check if this vertice has not been visited yet 
                    if not visitedObj[vertice]:
                    # and add the neighbor nodes of the next layer into the queue 
                    # new nodes to visit
                        neighborNodesToVisit.enqueue(self.vertices[vertice])
                        # indicate we need to visit it
                
                currentLayer = []
        
         # stop the BFT after there are no more objs in the queue
         # which means we can't visit anywhere else anymore'
        print(visitedNodes)

    def dft(self, starting_vertex):

        # question
        # if there is more than one neighbor to traverse after going to next layer
        # loop from left to right

        # Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
        # Pop the first vertex
            v = s.pop()
             # If that vertex has not been visited...
            if v not in visited:
            # Mark it as visited...
                print(v)
                visited.add(v)
            # Then add all of its neighbors to the top of the stack
                for next_vert in self.vertices[v]:
                    s.push(next_vert)

        print(visited)
        
    def dft_recursive(self, starting_vertex):
        
        s = Stack()
        visited = set()
        # if there is only one node; return this node 
        if self.vertices[starting_vertex].size == 0:
            visited.add(starting_vertex)
            return visited
        else:
            # add all child verticies in stack
            for vertice in self.vertices[starting_vertex]:
                s.add(vertice)
            while s.size() > 0:
                v = s.pop()
                # last in first out
                if v not in visited:
                    # conduct recursion per each individual chain, to see if each verticie has a child
                    visited.add(dft_recursive(v))
        # this maintains stack last out first in rule

        pass  # TODO
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO


graph1 = Graph()  # Instantiate your graph
graph1.add_vertex('0')
graph1.add_vertex('1')
graph1.add_vertex('2')
graph1.add_vertex('3')
graph1.add_edge('0', '1')
graph1.add_edge('0', '3')
print("StartTest")
print(graph1.vertices)
print("EndTest")



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
