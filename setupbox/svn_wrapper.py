import os
from vcs_wrapper import vcs_wrapper
import sqlite3, json
import pickle
from subprocess import Popen, PIPE


class svn_wrapper(vcs_wrapper):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def checkout(self, url, dest):
        self.do_command('checkout', [url, dest])
        os.chdir(dest)

    def getNewFiles(self):
        p = self.do_command('stat', [], True)

        assert len(p.stderr.read()) == 0

        output = str(p.stdout.read())

        output = output.split('\\n')

        result = []
        modified = False

        for line in output:
            temp = line.split()
            if len(temp) < 2:
                continue

            if temp[0] == '?':
                result.append(temp[1])

            if not modified:
                modified = True

        return result, modified

    def add(self, targets):
        self.do_command('add', [targets])

    def rm(self, targets):
        self.do_command('rm', [targets], True)

    def commit(self, msg):
        msg = '-m \"' + msg + '\"'

        self.do_command('commit', [msg])

    def push(self):
        pass

    def update(self):
        self.do_command('update', [], True)

    def revert(self):
        pass

    def cleanup(self):
        self.do_command('cleanup', [], True)

    def do_command(self, command, parameters=[], simple=False):
        username = self.username
        password = self.password

        vcs = 'svn'

        if simple:
            p = Popen([vcs, command], stdout=PIPE, stderr=PIPE)
            return p

        vcs += ' '
        vcs_command = command + " "

        parameter_str = ''

        for p in parameters:
            parameter_str = parameter_str + p + ' '

        options = " --non-interactive --trust-server-cert -q "

        if username is None:
            username = ''
        else:
            username = '--username ' + username + " "

        if password is None:
            password = ''
        else:
            password = '--password ' + password + " "

        command = vcs + vcs_command + parameter_str + options + username + password

        os.system(command)
