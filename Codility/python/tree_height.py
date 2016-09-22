# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/tree_height
# 100/100


class Tree(object):
    x = 0
    l = None
    r = None

    def __init__(self, x=0, l=None, r=None):
        super(Tree, self).__init__()
        self.x = x
        self.l = l
        self.r = r


def solution(T):
    def get_tree_depth(current_tree):
        if not current_tree:
            return -1

        return max(get_tree_depth(current_tree.l), get_tree_depth(current_tree.r)) + 1
    return get_tree_depth(T)


assert solution(Tree(5, Tree(3, Tree(20, None, None), Tree(21, None, None)), Tree(10, Tree(1, None, None), None))) == 2
assert solution(Tree(5, Tree(3, Tree(20, None, None), Tree(21, Tree(12, Tree(42, None, None)), None)), Tree(10, Tree(1, None, None), None))) == 4
assert solution(Tree(5, None, None)) == 0
assert solution(None) == -1
