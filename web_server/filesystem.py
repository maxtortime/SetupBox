# -*- coding: utf-8 -*-
from genericpath import isfile
import os
from os.path import join, basename, splitext, isdir, dirname, getmtime, getsize, sep
from action import View
import string
import time

def size_conversion(size):
        K = 1000

        if size > K:
            KB = str(size / K) + "KB"
            return KB

        elif size > pow(K,2):
            MB = str(size / pow(K,2)) + "MB"
            return MB

        elif size > pow(K,3):
            GB = str(size / pow(K,3)) + "GB"
            return GB

        elif size > pow(K,4):
            TB = str(size / pow(K,4)) + "TB"
            return TB

        elif size < K:
            return str(size) + "B"
        else:
            return "Too Large"

class Node(object):
    def __init__(self, root, path):
        splitedPath = string.split(path,"/")
        self.path = sep.join(splitedPath)
        self.root = root
        self.size = size_conversion(getsize(os.path.join(root, path)))
        self.date = time.ctime(getmtime(os.path.join(root, path)))
        self._basename = basename(self.path)

    def __unicode__(self):
        return self.name

    def get_actions(self):
        return self.avaliable_actions

    def apply_action(self, action_class):
        action = action_class(self)
        return action.apply()


class File(Node):
    avaliable_actions = [View, ]
    def __unicode__(self):
        return self.name

    @property
    def extension(self):
        return splitext(self._basename)[1][1:]

    @property
    def name(self):
        return self._basename

    def get_path(self):
        return dirname(self.path)


class Folder(Node):
    
    def __init__(self, root, path):
        super(Folder, self).__init__(root, path)
        self.files = []
        self.folders = []

    @property
    def name(self):
        return basename(self.path)

    def chunks(self):
        chunk_path = ''
        for chunk in self.path.split(os.sep):
            chunk_path = join(chunk_path, chunk)
            yield {'chunk': chunk, 'path': chunk_path}


    def read(self):
        for node in os.listdir(join(self.root, self.path)):
            full_path = join(self.path, node)
            if isdir(join(self.root, full_path)):
                self.folders.append(Folder(self.root, full_path))
            if isfile(join(self.root, full_path)):
                self.files.append(File(self.root, full_path))
