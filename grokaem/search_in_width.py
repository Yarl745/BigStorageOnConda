from collections import deque
# ----------------------------------------------------------------------------------------------------------------------
def search_in_width(graph, start_point, finish_point):
    graph_deque = deque()
    graph_deque += [(point, 1) for point in graph[start_point]]
    while graph_deque:
        print(graph_deque)
        cur_point = graph_deque.popleft()
        if cur_point[0] == finish_point:
            return 'The shortest way is {} steps'.format(cur_point[1])
        else:
            graph_deque += [(point, cur_point[1] + 1) for point in graph[cur_point[0]]]
    return 'The way from {} to {} is not exist!'.format(start_point, finish_point)
# ----------------------------------------------------------------------------------------------------------------------
graph = {
    'Kiev': ['Kharkiv', 'Odessa', 'Zaporozhie'],
    'Kharkiv': ['Zhytomyr'],
    'Odessa': ['Chernigiv'],
    'Zaporozhie': ['Vinecia'],
    'Vinecia': ['Crim'],
    'Chernigiv': ['Akimovka'],
    'Zhytomyr': ['Melitopol'],
    'Akimovka': ['Crim'],
    'Melitopol': ['Crim']
}
# ----------------------------------------------------------------------------------------------------------------------
print(search_in_width(graph, 'Kiev', 'Crim'))
