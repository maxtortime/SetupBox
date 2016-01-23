# -*- coding: utf-8 -*-
import os

class Action(object):
    """docstring for Action"""
    def __init__(self, node):
        self.node = node

class View(Action):
    """docstring for View"""
    def apply(self):
        try:
            text = unicode(open(os.path.join(self.node.root, self.node.path)).read())
        except UnicodeDecodeError:
            return None
        return { 'text' : text }

class Search(Action):
    def apply(self, folder_to_search_into, mask):
        founds = []
        for root, dirs, files in os.walk(folder_to_search_into, topdown=False):
            for name in files:
                if mask in name:
                    founds.append(os.path.join(root, name))
        return founds
