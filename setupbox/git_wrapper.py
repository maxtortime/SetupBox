import os
from setupbox import vcs_wrapper
from subprocess import Popen, PIPE

class git_wrapper(vcs_wrapper):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def checkout(self, url, dest):
        self.do_command('clone', [url, dest])
        os.chdir(dest)

    def add(self, targets):
        self.do_command('add', [targets])

    def rm(self, targets):
        self.do_command('rm', [targets])

    def commit(self, msg):
        msg = '-m \"' + msg + '\"'
        self.do_command('commit', [msg])

    def push(self):
        self.do_command('push', ['origin', 'master'])

    def update(self):
        self.do_command('pull', ['origin', 'master'])

    def revert(self):
        pass

    def do_command(self, command, parameters=[]):
        command_list = []

        vcs = 'git'
        command_list.append(vcs)
        vcs_command = command
        command_list.append(vcs_command)

        for p in parameters:
            command_list.append(p)

        p = Popen(command_list, stdout=PIPE, stderr=PIPE)
