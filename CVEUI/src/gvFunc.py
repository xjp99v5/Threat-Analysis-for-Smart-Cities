# -*- coding: utf-8 -*-
# @Time    : 2017/10/27 0:00
# @Author  : Jiaping Xiao
# @File    : gvFunc.py
def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph

def add_edges(graph, edges):
    # type: (object, object) -> object
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph