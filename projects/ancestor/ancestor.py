from util import Stack, Queue  # These may come in handy

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.ancestors = {}

    def earliest_ancestor(self, ancestors, starting_node):

        # step 1)

        # organize the dataset into a graph
        # (parent, child) // we know this about data type
        # REFACTORING STEP

        # ensure that you have layers of grandparents, parents, child
        # to prevent the earliest ancestor from being a cousin
        # by virtue of having lots of uncles and aunts

        for parentChild in ancestors:
            parent = parentChild[0]
            child = parentChild[1]

            # parent has more than one child
            if self.ancestors[parent]:
                self.ancestors[parent].append(child)
            else:
                self.ancestors[parent] = [child] 

        # step 2)

        # store allPossiblePaths in a cache (array) 
        allPossiblePaths = []

        # longest path means use depth first search to find the 
        # earliest ancestor
        # set up the algorithim to allow for accessing parents

        # use a while loop that stops once the queue is zero
        s = Stack()
        s.push([starting_node])

        visited = []
         # path = []
 
         # make sure current vertex does not equal destination vertex
        while s.size() > 0: 
            path = s.pop()
            currentChild = path[-1]
 
            if currentChild not in visited:
                visited.append(currentChild)

                parentsOfCurrentChild = []

                # search for all parents for child
                for parent in self.ancestors:
                    if currentChild in self.ancestors[parent]:
                        parentsOfCurrentChild.append(parent)

                # if he or she has no parents, we've hit the end of the path
                
                if len(parentsOfCurrentChild) == 0:
                    allPossiblePaths.append(path)
                else: 
                    # then add possible paths to traverse upwards
                    for parent in parentsOfCurrentChild:
                        newPath = list(path)
                        # add the path of one OR both parents into stack
                        newPath.append(parent)
                        s.push(newPath)
        
        allPossiblePaths = sorted(allPossiblePaths)
        longestPath = allPossiblePaths[-1]
        return longestPath

s = SocialGraph()




