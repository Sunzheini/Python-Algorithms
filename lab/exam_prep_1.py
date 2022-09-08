# 01. The story telling (Graph using dfs)
# from collections import deque


# def dfs(node, graph, visited):
#     if node in visited:
#         return
#     visited.add(node)
#     for child in graph[node]:
#         dfs(child, graph, visited)
#     result.appendleft(node)


# graph = {}
# result = deque()
# while 1:
#     line = input()
#     if line == 'End':
#         break

#     node, children_str = [x.strip() for x in line.split('->')]
#     children = children_str.split()
#     graph[node] = children

# visited = set()

# for node in graph:
#     dfs(node, graph, visited)

# print(' '.join(result))


# Task Input:
# Mort -> Time Space
# Time -> Future Robot
# Space -> Metro
# Future -> Space Metro
# Robot -> Future
# Metro ->
# End

# -----------------------------------------------------------------------------
# 2






# Task Input:
# 13 42 69 73 42 84 26
# 13 54 73 42 8 15 29

# -----------------------------------------------------------------------------
# 3




