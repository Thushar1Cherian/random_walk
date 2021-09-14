import random


def noode_chooser(added, neighbours):
    """Randomly chooses a node from the list of avaliable non traversed nodes

    Args:
        added ([type]): nodes that are already travelled
        neighbours ([type]): neoghbours of the node currently reached

    Returns:
        [graph.nodes]: random node picked from the list of avaliable nodes
        [integer]: a value of -777 is returned if all neighbouring nodes are removed
    """
    left_nodes = list(set(neighbours) - set(added))
    if len(left_nodes) == 0:
        return -666
    return random.choice(left_nodes)


def walker(graph, nodes_required=10):
    """Starts at a random node and moves to one of its neighbours at each step.
    All neighbours are given equal probability of being chosen.

    Args:
        graph ([type]): NetworkX graph
        nodes_required (int, optional): Number of nodes required in the final random walked graph. Defaults to 10.

    Returns:
        [list]: list of nodes traveresed.
    """
    nodes_in_graph = len(graph.nodes())
    if nodes_in_graph < nodes_required:
        raise ValueError(
            "The number of nodes required in the traversed\
        graph is less than the total number of nodes"
        )
    else:
        nodes = []
        travelled = []
        for node in graph.nodes():
            nodes.append(node)
        first_node = random.choice(nodes)
        travelled.append(first_node)
    return travelled
