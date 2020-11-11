from .queue import Queue

class Node:
    def __init__(self, state, parent_node=None, action=None, path_cost=0, depth=0, successors=[]):
        self.state = state
        self.parent_node = parent_node
        self.action = action
        self.path_cost = path_cost
        self.depth = depth
        self.successors = successors
        self.visited = False

    def __str__(self):
        result_string = ''
        result_string += 'state: ' + str(self.state) + '\n'
        if self.parent_node is not None:
            result_string += 'parent_node: ' + str(self.parent_node.state) + '\n'
        else:
            result_string += 'parent_node: ' + 'None' + '\n'
        result_string += 'action: ' + str(self.action) + '\n'
        result_string += 'path_cost: ' + str(self.path_cost) + '\n'
        result_string += 'depth: ' + str(self.depth) + '\n'
        result_string += 'successors: ' + str(len(self.successors)) + '\n'
        return result_string

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


def create_successors(node, node_connections, cost=None):
    successors = []
    for connection in node_connections[str(node.state)]:
        new_node_cost = 0
        if (cost is not None):
            new_node_cost = node.path_cost+cost[str(node.state) + ' ' + str(connection)]
        new_node_depth = node.depth+1
        new_node_action = str(node.action)+' '+str(connection)
        new_node_state = connection
        successors.append(Node(new_node_state, node, new_node_action, new_node_cost, new_node_depth))

    return successors


def check_loop(node, successor):
    if (node.parent_node is not None and str(successor.state) in node.parent_node.action):
        return False
    return True


def check_successors(node, successors):
    passed = []
    functions = [check_loop]
    for s in successors:
        flag = True
        for f in functions:
            res = f(node, s)
            flag = flag and res   
        if flag:
            passed.append(s)
    return passed


def build_tree_from_info(start_point, node_connections, cost=None):
    print('Building tree')
    q = Queue()
    root = Node(start_point, action=str(start_point), path_cost=0)
    q.insert(root)
    count = 0
    while not q.empty():
        node = q.remove_first()
        if not node.visited:
            count += 1
            successors = create_successors(node, node_connections, cost)
            successors = check_successors(node, successors)
            node.set_successors(successors)
            node.visited = True
            q.insert_all(successors)
    return root


def width_search(root, target):
    print('Finding route with width search')
    q = Queue()
    q.insert(root)
    while not q.empty():
        node = q.remove_first()
        if (node.state == str(target)):
            return node
        q.insert_all(node.successors)

    return None


def a_star_search(root, target, h):
    def f(node):
        return node.path_cost + h[str(node.state)]

    q = Queue()
    q.insert(root)
    while not q.empty():
        node = q.remove_first()
        if (str(node.state) == str(target)):
            return node

        min_dist = f(node.successors[0])
        min_node = node.successors[0]
        for s in node.successors:
            s_dist = f(s)
            if s_dist < min_dist:
                min_dist = s_dist
                min_node = s
        q.insert(min_node)