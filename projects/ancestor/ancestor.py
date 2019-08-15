from util import Stack, Queue  # These may come in handy


def earliest_ancestor(ancestorsData, starting_node):

    ancestors = {}
        # step 1)

        # organize the dataset into a graph
        # (parent, child) // we know this about data type
        # REFACTORING STEP

        # ensure that you have layers of grandparents, parents, child
        # to prevent the earliest ancestor from being a cousin
        # by virtue of having lots of uncles and aunts

    for parentChild in ancestorsData:
        parent = parentChild[0]
        child = parentChild[1]

            # parent has more than one child
        if parent in ancestors.keys():
            ancestors[parent].append(child)
        else:
            ancestors[parent] = [child] 

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
            for parent in ancestors:
                if currentChild in ancestors[parent]:
                    parentsOfCurrentChild.append(parent)

                # if he or she has no parents, we've hit the end of the path
                
            if len(parentsOfCurrentChild) == 0:
                    # store this path into allPossiblePaths
                allPossiblePaths.append(path)
            else: 
                    # if he / she has parents, time to add those paths onto the stack
                    # for further traversing up the ladder
                for parent in parentsOfCurrentChild:
                    newPath = list(path)
                        # add the path of one OR both parents into stack
                    newPath.append(parent)
                    s.push(newPath)
        

        # step 3) after compiling all possible paths using DFS, sort them to find the longest path
    allPossiblePaths = sorted(allPossiblePaths)
    print("All possible paths", allPossiblePaths)
    longestPath = allPossiblePaths[0]
    earliestAncestor = longestPath[-1]
    if earliestAncestor == starting_node:
        return -1
    else:
        return earliestAncestor

parentsChild = [  
  [1,3],
  [2,3],
  [3,6],
  [5,6],
  [5,7],
  [4,5],
  [4,8],
  [8,9],
  [11,8],
  [10,1]
]

g = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(parentsChild,6))
