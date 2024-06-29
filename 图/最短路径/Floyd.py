def Floyd(graph):
    # 顶点数目
    Vn = len(graph)
    # 初始化最小距离
    dist = [[graph[i][j] for j in range(Vn)]for i in range(Vn)]
    # 动态规划遍历最短路径
    for k in range(Vn):
        for i in range(Vn):
            for j in range(Vn):
                dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
    return dist

# 参数示例
graph = [
    [0,50,float('inf'),40,25,10],
    [50,0,15,20,float('inf'),25],
    [float('inf'),15,0,10,20,float('inf')],
    [40,20,10,0,10,25],
    [25,float('inf'),20,10,0,55],
    [10,25,float('inf'),25,55,0]
]

