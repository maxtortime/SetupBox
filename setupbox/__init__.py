# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from git import Repo


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


class VcsCoreGit(VcsCore):
    def __init__(self, repo_dir):
        self.repo = Repo.init(repo_dir)

    def __del__(self):
        pass

    def update(self):
        git = self.repo.git

    def commit(self, msg):
        git = self.repo.git
        git.add('.')
        git.commit(msg)
        # git.push() is not executed because git config is not completed

    def add(self, filename):
        git = self.repo.git
        git.add(filename)

VcsCore.register(VcsCoreGit)
