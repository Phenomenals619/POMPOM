def alpha_beta(node, depth, alpha, beta, maximizing_player):
    """
    Perform the alpha-beta pruning algorithm.
    
    :param node: The current node in the game tree
    :param depth: The maximum depth to search
    :param alpha: The best value that the maximizing player can guarantee so far
    :param beta: The best value that the minimizing player can guarantee so far
    :param maximizing_player: Boolean indicating whether the current move is for the maximizing player
    :return: The best value of the current node
    """
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximizing_player:
        value = float('-inf')
        for child in node.get_children():
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = float('inf')
        for child in node.get_children():
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

# Example usage
class Node:
    def __init__(self, is_terminal=False, value=0):
        self.is_terminal = is_terminal
        self.value = value
        self.children = []

    def is_terminal(self):
        return self.is_terminal

    def evaluate(self):
        return self.value

    def get_children(self):
        return self.children

# Create nodes for testing
node1 = Node(is_terminal=True, value=3)
node2 = Node(is_terminal=True, value=5)
node3 = Node(is_terminal=True, value=2)
node4 = Node(is_terminal=True, value=9)

parent_node = Node()
parent_node.children = [node1, node2]
node1.children = [node3, node4]

# Running alpha-beta search
best_value = alpha_beta(parent_node, 2, float('-inf'), float('inf'), True)
print("Best value:", best_value)
