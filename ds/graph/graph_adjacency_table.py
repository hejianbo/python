from ds.graph.edge import Edge

"""
图结点
"""
class VertexNode(object):
    def __init__(self):
        # 顶点数
        self.vertex_number = 0
        # 边数
        self.edge_number = 0
        # 邻接表
        self.first_edge = None
        # 顶点数据
        self.data = None

"""
邻接顶点
"""
class AdjacencyVertexNode(object):
    def __init__(self, vertex_index, weight):
        self.vertex_index = vertex_index
        self.weight = weight
        self.next_edge = None

class GraphAdjacencyTable(object):
    def __init__(self, vertex_number):
        # 顶点数
        self.vertex_number = vertex_number
        # 边数
        self.edge_number = 0
        # 初始化
        self.data = [VertexNode() for i in vertex_number]

    def add_edge(self, edge):
        # 根据边的v2创建邻接结点
        adj_node = AdjacencyVertexNode(edge.v2, edge.weight)
        # 将结点放入到链表头
        node = self.data[edge.v1]
        adj_node.next_edge = node.first_edge
        node.first_edge = adj_node

        # 如果是无向图

if __name__ == "__main__":
    vertex_number = 10
    # 定义10个结点的邻接表
    graph = GraphAdjacencyTable(vertex_number)

    # 边数
    edge_number = 10
    # 插入边
    for i in range(edge_number):
        edge = Edge()
        graph.add_edge(edge)
       
    # 设置顶点数据
    for i in range(vertex_number):
        graph.data[i].data = None