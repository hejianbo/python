"""
边定义
"""
class Edge(object):
    def __init__(self, v1, v2, weight):
        # 顶点
        self.v1 = v1
        self.v2 = v2
        # 权重
        self.weight = weight