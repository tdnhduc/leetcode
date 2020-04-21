#!/usr/bin/env python3.8

class Node:
    def __init__(self, value = None):
        self.value = value
        self.leftNode = None
        self.rightNode = None
class Tree:

    def __init__(self, root = None):
        self.root = root

    def genarate(self, value_nodes):
        self.root = Node(value=value_nodes[0])
        self.addListNode(self, value_nodes[1:])

    def addNode(self, value, current_node):
        if value <= current_node.value:
            current_node.leftNode = Node(value=value)
        else:
            current_node.rightNode = Node(value=value)
        return current_node

    def traversal(self, node):
        if node is None:
            return
        elif node.leftNode is not None:
            self.traversal(node.leftNode)
        elif node.rightNode is not None:
            self.traversal(node.rightNode)

    def addListNode(self, root, value_list):
        for value in value_list:
            tmp = self.root
            while tmp is not None:
                if value <= tmp.value and tmp.leftNode is not None:
                    tmp = tmp.leftNode
                if value > tmp.value and tmp.rightNode is not None:
                    tmp = tmp.rightNode
              


class Solution:

    def generate_binaryTree(self, candidates):
        pass

    def combinationSum(self, candidates, target):
        candidates = candidates.sort()
        result = []

        if target in candidates:
            result.append(candidates)
    
    def recursion(self, subcandicates, number, target, sum_candidate):
        if sum_candidate > target:
            return sum_candidate
        