from .queue import Queue

class Node:
    def __init__(self, state, parent_node=None, action=None, path_cost=[], depth=0, successors=[]):
        self.state = state
        self.parent_node = parent_node
        self.action = action
        self.path_cost = path_cost
        self.depth = depth
        self.successors = successors

    def set_successors(self, new_successors):
        self.successors = new_successors

    def is_equal_to(self, node):
        return self.state == node.state

    def has_successors(self):
        return len(self.successors) != 0

    def path_to_root_node(self):
        previous_nodes = []
        previous_node = self.parent_node
        while (previous_node != None):
            previous_nodes.append(previous_node)
            previous_node = previous_node.parent_node

        return previous_nodes


def create_successors(node, node_connections):
    successors = []
    new_node_path = node.path_to_root_node().append(node)
    for connection in node_connections[node.state]:
        new_node_depth = node.depth+1
        new_node_action = node.state+connection
        new_node_state = connection
        successors.append(Node(new_node_state, node, new_node_action, new_node_path, new_node_depth))

    return create_successors

def check_reverse_action(node, successor):
    return node.parent_node.is_equal_to(successor)

def check_loop(node, successor):
    for previous_node in node.path_to_root_node():
        if previous_node.is_equal_to(successor):
            return True
    return False

def check_successors(node, successors):
    passed = []
    for s in successors:
        if not (check_reverse_action(node, s) or check_loop(node, s)):
            passed.append(s)
    return passed

def build_tree_from_info(start_point, node_connections):
    q = Queue()
    root = Node(start_point, Node)
    q.insert(root)
    while not q.empty():
        node = q.remove_first()
        successors = create_successors(node, node_connections)
        successors = check_successors(node, successors)
        node.set_successors(successors)
        q.insert_all(successors)

    return root