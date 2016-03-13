import json
from subprocess import Popen, PIPE

import os
from setupbox import vcs_wrapper

setupbox_dir = './.sb'
tracking_file = setupbox_dir + '/tracking.json'
transaction_file = setupbox_dir + '/transaction.txt'

class svn_wrapper(vcs_wrapper):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.transactions = []

#        if os.path.exists(setupbox_dir) == False:
#            os.mkdir(setupbox_dir)
        
#        if os.path.exists(tracking_file):
#            with open(tracking_file, 'r') as f:
#                dumps = f.read()
#                self.tracking = json.loads(dumps)
#        else:
#            self.tracking = {}

    def flush(self):
        with open(transaction_file, 'wt') as f:
            dumps = json.dumps(self.transactions)
            f.write(dumps)

    def checkout(self, url, dest):
        # url = url + '/trunk'
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
        # if os.path.isdir(targets):
            # dentries = os.listdir(targets)

            # for dentry in dentries:
              #  self.tracking[dentry] = dentry
        # else:
          #  self.tracking[targets] = targets

        # self.transactions.append(['add', [targets]])

        self.do_command('add', [targets])

    def rm(self, targets):
        self.do_command('rm', [targets], True)

    def commit(self, msg):
        msg = '-m \"' + msg + '\"'

        # self.transactions.append(['commit', [msg]])
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
