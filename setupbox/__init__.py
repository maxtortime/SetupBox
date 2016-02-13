# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class VcsCore:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def add(self, filename):
        pass

    @abstractmethod
    def commit(self, msg):
        pass

class VcsCoreSvn(object):
    def __init__(self, repo_dir):
        pass




VcsCore.register(VcsCoreSvn)
