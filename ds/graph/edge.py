"""
边定义
"""
class Edge(object):
    def __init__(self, start_vertex, end_vertex, weight):
        # 顶点
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        # 权重
        self.weight = weight