from routetab import RouteTable
from util import randomid
from node import Node


if __name__ == '__main__':
    node_id = randomid()
    tab = RouteTable(node_id)
    for i in range(2 ** 20):
        tab.insert(Node(randomid(), i))
    for node in tab.get_neighbor(node_id):
        print(node)
