
import random
from util import Stack, Queue  # These may come in handy

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def getAllSocialPaths(self, userId):

        # for degrees of separation

        # breadth first search
        # for each friend

        allPaths = {}
        
        for friend_id in self.users:
            allPaths[friend_id] = []

        for friend_id in allPaths:  

            # queue system for neighbors:
            friends = Queue()
            friends.enqueue([userId])

            visited = []
            # path = []

            # make sure current vertex does not equal destination vertex
            while friends.size() > 0: 
                path = friends.dequeue()
                currentFriend = path[-1]

                if currentFriend not in visited:
                    if currentFriend == friend_id:
                        allPaths[friend_id] = path 
                        break
                    visited.append(currentFriend)
                # the breadth first search will be looking for the shortest "cake", or layer that leads us to the destination vertex
                # if neighborNodesToVisit.size == 0:
                    for friend in self.friendships[currentFriend]:

                        new_path = list(path)
                        new_path.append(friend)
                        friends.enqueue(new_path)
                # this code will break id currentVertex is destination_vertex
        
        totalLengths = 0

        for path in allPaths:
            totalLengths += len(allPaths[path])

        averageDegreesOfSep = totalLengths/len(allPaths)
        return averageDegreesOfSep
        
    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
    
        Creates that number of users and a randomly distributed friendships
        between those users.
    
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
            # !!!! IMPLEMENT ME
            
            # Add users
        for i in range(numUsers):
            self.addUser(f'User {i+1}')
    
            # Create friendships
        # avgFriendships = totalFriendships / numUsers
        # totalFriendships = avgFriendships * numUsers
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))
    
        random.shuffle(possibleFriendships)
    
        for friendship_index in range(avgFriendships * numUsers // 2):
            friendship = possibleFriendships[friendship_index]
            self.addFriendship(friendship[0], friendship[1])

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    # print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print("Degrees of Separation", connections)
