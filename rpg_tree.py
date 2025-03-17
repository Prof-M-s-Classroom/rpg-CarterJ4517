class StoryNode:
    """Represents a node in the decision tree."""
    def __init__(self, event_number, description, left=None, right=None):
        # print(f"TODO: Initialize StoryNode with event_number={event_number}, description={description}")
        # TODO: Initialize instance variables (event_number, description, left, right)
        self.event_number = event_number
        self.description = description

class GameDecisionTree:
    """Binary decision tree for the RPG."""
    def __init__(self):
        # print("TODO: Initialize an empty decision tree")
        # TODO: Initialize an empty dictionary to store nodes
        # TODO: Set root to None
        self.nodes = {}
        self.root = None

    def insert(self, event_number, description, left_event, right_event):
        """Insert a new story node into the tree."""
        # print(f"TODO: Insert event {event_number} with description '{description}' into the tree")
        # TODO: Check if event_number exists in self.nodes, if not create a new StoryNode
        # TODO: Assign left and right children based on left_event and right_event
        # TODO: Set root if it's the first node inserted
        if not(event_number in self.nodes):
            temp = StoryNode(event_number, description, left_event, right_event)
            if self.root is not None:
                self.nodes[event_number] = temp
            else:
                self.root = temp

    def play_game(self):
        """Interactive function that plays the RPG."""
        # print("TODO: Implement the game logic for traversing the decision tree")
        # TODO: Start from the root node
        # TODO: Loop through player choices, navigating left or right based on input
        # TODO: Print event descriptions and ask for player decisions
        # TODO: End game when reaching a leaf node (where left and right are None)
        temp = self.root
        while temp is not None:
            print(temp.description)
            decision = input("What do you choose?")
            flag = 0
            while flag == 0:
                if decision == 1:
                    flag = 1
                    temp = self.nodes[temp.left]
                elif decision == 2:
                    flag = 1
                    temp = self.nodes[temp.right]
                else:
                    decision = input("Please type either '1' or '2'")

def load_story(filename, game_tree):
    """Load story from a file and construct the decision tree."""
    # print(f"TODO: Read story file '{filename}' and parse events")
    # TODO: Open the file and read line by line
    # TODO: Split each line into event_number, description, left_event, right_event
    # TODO: Call game_tree.insert() for each event to build the tree
    with open('story.txt', 'r') as file:
        line = file.readline()
        while line:
            substrings = line.split(' | ')
            event_number = int(substrings(1))
            description = substrings(2)
            left_event = int(substrings(3))
            right_event = int(substrings(4))
            game_tree.insert(event_number, description, left_event, right_event)
            line = file.readline()

# Main program
if __name__ == "__main__":
    print("TODO: Initialize the GameDecisionTree and load story data")
    game_tree = GameDecisionTree()

    print("TODO: Load the story from 'story.txt'")
    load_story("story.txt", game_tree)

    print("TODO: Start the RPG game")
    game_tree.play_game()