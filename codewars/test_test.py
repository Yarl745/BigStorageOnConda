graph = {
    'start': {'A': 6, 'B': 2},
    'B': {'A': 3, 'finish': 5},
    'A': {'finish': 1}
}
def dijkstra_search(graph: dict, start_point: str):
    shortest_roads = {}
    fill_shortest_roads(graph[start_point], shortest_roads)


def fill_shortest_roads(graph_el: dict, shortest_roads: dict):
    for key, value in graph_el.items():
        if shortest_roads.get(key) is None:
            shortest_roads[key] = value
        else:
            if value < shortest_roads[key]: shortest_roads[key] = value

def include_road_graph_el(graph_el: dict, road_to_graph_el: int):
    for key, value in graph_el: graph_el[key] = value + road_to_graph_el


# def sort_graph

# print(graph.get('startt'))



