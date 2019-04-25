# coding = utf-8 
# python 3.6.7 
# Created by wuyang at2019/1/20

import time
import read_and_create_graph_dataset as rgd


def BFS(graph):
    """
        基于BFS的拓扑排序
        1. 标记图graph中的没有访问所有节点
        2. 令初始的拓扑序列为空
        3. 计算每一个节点的入度数，把入度为0的节点放到一个队列BFS_sort_head中，并标记节点已经被访问
        4. 执行BFS操作，当队列BFS_sort_head不为空时，执行第5步；否则执行第6步
        5. 当队列BFS不为空，循环执行下面的操作
            5.1 取出队头元素head，把head插入到拓扑序列BFS_sort中
            5.2 遍历head的所有相邻节点v
                5.2.1 令v的入度减1
                5.2.1 若v的入度数变为0，则把v插入到队列BFS_sort_head中，并标记v已被访问
                5.2.3 继续遍历下一个邻节点
        6. 得到最终的拓扑排序BFS_sort

        graph：传入的需要用BFS遍历的有向图
    """
    node_in_degree = graph.in_degree
    node_in_degree_mapdict = {}  # 各节点的入度信息，字典类型，key为节点，value为入度值
    for node_in_degree_item in node_in_degree:
        node_in_degree_mapdict[node_in_degree_item[0]] = node_in_degree_item[1]
    out_neighbour, in_neighbour, both_neighbour = rgd.get_neighbor(graph)
    BFS_sort_head = []
    for node in graph.nodes:
        if node_in_degree_mapdict[node] == 0:
            BFS_sort_head.append(node)
    BFS_sort = []
    while len(BFS_sort_head) != 0:
        BFS_sort.append(BFS_sort_head[0])
        for neighbour in out_neighbour[BFS_sort_head[0]]:
            if (node_in_degree_mapdict[neighbour]-1) == 0:
                BFS_sort_head.append(neighbour)
            else:
                node_in_degree_mapdict[neighbour] = node_in_degree_mapdict[neighbour]-1
        BFS_sort_head.pop(0)
    return BFS_sort


if __name__ == "__main__":
    start_time = time.time()
    dataset_path_00 = "F:\\Windows10\\Desktop\\the dataset of DeepGL\\frb30-15-1.txt"
    dataset_path_01 = r"F:\Windows10\Desktop\ia-email-EU-dir\ia-email-EU-dir.edges"
    dataset_path_02 = r"F:\Windows10\Desktop\01.txt"
    graph = rgd.read_and_create_without_weight_graph(dataset_path=dataset_path_00, direct=1)
    BFS_sort = BFS(graph)
    print("BFS_sort:\n{}\nBFS_sort_len:\n{}\n".format(BFS_sort, len(BFS_sort)))
    end_time = time.time()
    print("总耗时：\n %f s" % (end_time-start_time))
