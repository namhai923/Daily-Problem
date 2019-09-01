def find_cycle(graph):

graph = {
    'a': {'a2':{}, 'a3':{} },
    'b': {'b2':{}},
    'c': {}
}
print(find_cycle(graph))
graph['c'] = graph
print(find_cycle(graph))