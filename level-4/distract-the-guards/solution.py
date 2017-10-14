max_count = 0
def answer(banana_list):
    if len(banana_list) < 2:
        return 0
    graph = [[] for _ in banana_list]
    for index, a in enumerate(banana_list):
        for j in range(index, len(banana_list)):
            b = banana_list[j]
            if a > b:
                isTricky = isTrickyPair(a, b)
            else:
                isTricky = isTrickyPair(b, a)
            if isTricky:
                graph[index].append(j)
                graph[j].append(index)

    maxPossible(graph, [False for _ in banana_list])
    return len(banana_list) - 2*max_count

def isTrickyPair(a, b, states = set()):
    if a == b:
        return False
    key = (a, b)
    if key in states:
        return True
    states.add(key)
    mul = int(a / b)
    mul = int((mul + 1) / 2)
    mul = 2**(len(bin(mul)) - 3)
    a = a - (mul * b) + b
    b = (mul * b)
    if b > a:
        a, b = b, a
    return isTrickyPair(a, b, states)

def maxPossible(graph, seen):
    for index, val in enumerate(seen):
        if not val:
            seen[index] = True
            traverse(graph, index, seen, 0)

def traverse(graph, index, seen, count):
    global max_count
    for node_index in graph[index]:
        if not seen[node_index]:
            seen[node_index] = True
            count += 1
            for other_node_index in graph[index]:
                if not seen[other_node_index]:
                    seen[other_node_index] = True
                    traverse(graph, other_node_index, seen, count)
            seen[node_index] = False
            max_count = max(max_count, count)
            count -= 1

l = [1,2,3,4,5,6,7,8,9]
print(answer(l))
# for i, a in enumerate(l):
#     for j in range(i+1, len(l)):
#         b = l[j]
#         if b > a:
#             a, b = b, a
#         print(a, b, isTrickyPair(a, b))
#
# # print(isTrickyPair(7, 1))
