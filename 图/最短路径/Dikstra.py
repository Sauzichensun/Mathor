import heapq

def dijkstra(graph, start):
    # 优先队列，用于存储 (距离, 顶点) 元组
    priority_queue = []
    # 字典，用于存储从起点到每个顶点的最短路径距离
    distances = {vertex: float('infinity') for vertex in graph}
    parent = {vertex:-1 for vertex in graph}
    # 起点的距离为0
    distances[start] = 0
    # 将起点加入优先队列
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        # 弹出优先队列中距离最小的顶点
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # 如果弹出的顶点距离不是最小的，则继续
        if current_distance > distances[current_vertex]:
            continue

        # 遍历当前顶点的邻居
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # 如果发现到邻居的更短路径
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

# 返回从start到各个点的最小距离，以及路径来源
    return distances,parent

# 单一路径寻找最短距离
def multi_minwaylong(graph, start, end):
    distance,parent= dijkstra(graph, start)
    print(f"from {start} to {end}\nthe minest way is {distance[end]}")
    stl = []
    stl.append(end)
    while parent[end] != -1:
        stl.append(parent[end])
        end = parent[end]
    print(stl[::-1])

# 多源路径匹配距离
def all_match(graph,d):
    for i in graph:
        distances,parents= dijkstra(graph,i)
        for j in distances:
            if distances[j]==d:
               multi_minwaylong(graph,i,j)



# 示例图
graph = {
    'c1':{'c2': 50, 'c4': 40, 'c5': 25, 'c6': 10},
    'c2':{'c1': 50, 'c3': 15, 'c4': 20, 'c6': 25},
    'c3':{'c2' : 15,'c4' : 10,'c5': 20},
    'c4':{'c1': 40, 'c2': 20,'c3':10,'c5':10,'c6':25},
    'c5':{'c1':25,'c3':20,'c4':25,'c6':55},
    'c6':{'c1':10,'c2':25,'c4':25,'c5':55}
}

