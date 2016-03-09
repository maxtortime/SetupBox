import os
from vcs_wrapper import vcs_wrapper

class git_wrapper(vcs_wrapper):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def checkout(self, url, dest):
        self.do_command('clone', [url, dest]) 

    def add(self):
        pass

    def rm(self, targets):
        self.do_command('rm', [targets])

    def do_command(self, command, parameters=[]):
        username = self.username
        password = self.password

        vcs = 'git '
        vcs_command = command + ' '

        parameter_str = ''

        for p in parameter_str:
            parameter_str = parameter_str + p + ' '

        command = vcs + vcs_command + parameter_str

        os.system(command)