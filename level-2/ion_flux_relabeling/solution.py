def answer(h, q):
    p = []
    for n in q:
        node_height, is_left_child = getNodeInfo(n)
        p.append(getParent(n, node_height, is_left_child, h))
    return p

def getParent(n, node_height, is_left_child, tree_height):
    if node_height == tree_height:
        return -1
    if is_left_child:
        return n + 2**node_height
    else:
        return n + 1

def getNodeInfo(node):
    n = node + 1
    height = n.bit_length() - 1
    perfect_root_node = 2 ** height - 1
    if perfect_root_node == node:
        return height, True
    elif node == 2 * perfect_root_node:
        return height, False
    new_node = node - perfect_root_node
    return getNodeInfo(new_node)
