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

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('One or both of those vertices do not exist.')
  

    def bft(self, starting_vertex):
        # Create an empty stack and push the starting vertex ID
        q = Stack()
        q.push(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while q.size() > 0:
         # Pop the first vertex
            v = q.pop()
            if v not in visited:
            # Mark it as visited...
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the top of the stack
                for next_vert in self.vertices[v]:
                    q.push(next_vert)
       
    def dft(self, starting_vertex):

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
        if len(self.vertices[starting_vertex]) == 0:
            visited.add(starting_vertex)
            return visited
        else:
            # add all child verticies in stack
            for vertice in self.vertices[starting_vertex]:
                s.push(vertice)
            while s.size() > 0:
                v = s.pop()
                # last in first out
                if v not in visited:
                    # conduct recursion per each individual chain, to see if each verticie has a child
                    visited.add(dft_recursive(v))
        # this maintains stack last out first in rule
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # condition to check 
        currentVertex = starting_vertex

        # queue system for neighbors:
        neighborNodesToVisit = Queue()

        visited = set()
        # path = []

        # make sure current vertex does not equal destination vertex
        while currentVertex != destination_vertex: 
            path = neighborNodesToVisit.dequeue()
            currentVertex = path[-1]

            if currentVertex not in visited:
                if currentVertex == destination_vertex:
                    return path 
                visited.add(node)
            # the breadth first search will be looking for the shortest "cake", or layer that leads us to the destination vertex
            # if neighborNodesToVisit.size == 0:
                for vertice in self.vertices[currentVertex]:

                    new_path = list(path)
                    new_path.append(vertice)
                    neighborNodesToVisit.enqueue(new_path)
            # this code will break id currentVertex is destination_vertex

        # after hitting destination vertex, go backwards to calculate the path needed to reach

        # choose the path based on already visited breadth search path, avoid nodes that were not visited. 
        # while currentVertex != starting_vertex:
        #     for vertice in self.vertices[currentVertex]:
        #         if vertice in visited:
        #             currentVertex = vertice
        #             path.append(currentVertex)
        #             break 
        
        # make sure the parent verticies have been visited to add to the path

        # return the path 
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()


        # what is considered shortest
        # keep track of all possible paths
        
        # count the length of each path
        # return the shortest path

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
