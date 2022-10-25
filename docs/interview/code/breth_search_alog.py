#!/usr/bin/python3
# ▶️  python3 breth_search_alog.py

from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'ivan', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = ['tester']
graph['ivan'] = ['sre']

def person_is_seller(name):
    return name == 'sre'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft() # pop() for deep first search
        print(search_queue, person)
        if not person in searched: # only search this person if you haven't already search them
            if person_is_seller(person):
                print(f'{person} is a mango seller')
                return True
            else:
                if person in graph:
                    search_queue += graph[person]
                searched.append(person)
    return False

sgraph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print(graph)
search('you')

# print(sgraph)
# dfs(visited, sgraph, 'A')
