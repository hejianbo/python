"""
基于邻接矩阵实现图
"""
class GraphAdjacencyMatrix(object):
    def __init__(self, vertex_number):
        # 图顶点数
        self.vertex_number = vertex_number
        # 边数默认为0
        self.edge_number = 0
        # 初始化矩阵, 二维数组的每个位置都为None
        self.matrix = [[None for j in range(vertex_number)] for i in range(vertex_number)]
        # 存顶点的数据
        self.vertexs = []

    def add_edge(self, edge):
        self.matrix[edge.v1][edge.v2] = edge.weight
        # 如果是无向图，则2边都要初始化
        self.matrix[edge.v2][edge.v1] = edge.weight

"""
创建图
"""
if __name__ == "__main__":
    # 初始化一个空的邻接矩阵
    graph = GraphAdjacencyMatrix()

    vertex_number = 0
    edge_number = 0
    edges = []
    vertex = []

    # 设置边
    for edge in edges:
        graph.add_edge(edge)

    # 设置顶点数据
    for i in range(len(vertex)):
        graph.vertexs[i] = vertex[i]