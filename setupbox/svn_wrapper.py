import os
from vcs_wrapper import vcs_wrapper
import sqlite3, json
import pickle

setupbox_dir = './.sb'
tracking_file = setupbox_dir + '/tracking.json'
transaction_file = setupbox_dir + '/transaction.txt'

class svn_wrapper(vcs_wrapper):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.transactions = []

        if os.path.exists(setupbox_dir) == False:
            os.mkdir(setupbox_dir)
        
        if os.path.exists(tracking_file):
            with open(tracking_file, 'r') as f:
                dumps = f.read()
                self.tracking = json.loads(dumps)
        else:
            self.tracking = {}

    def flush(self):
        with open(transaction_file, 'wt') as f:
            dumps = json.dumps(self.transactions)
            f.write(dumps)

    def checkout(self, url, dest):
        url = url + '/trunk'
        self.do_command('checkout', [url, dest])

    def add(self, targets):
        if os.path.isdir(targets):
            dentries = os.listdir(targets)

            for dentry in dentries:
                self.tracking[dentry] = dentry
        else:
            self.tracking[targets] = targets

        self.transactions.append(['add', [targets]])
        self.do_command('add', [targets])

    def rm(self, targets):
        self.do_command('rm', [targets])

    def commit(self, msg):
        msg = '-m \"' + msg + '\"'

        self.transactions.append(['commit', [msg]])
        self.do_command('commit', [msg])

    def push(self):
        pass

    def update(self):
        self.do_command('update', [])

    def revert(self):
        pass

    def do_command(self, command, parameters=[]):
        username = self.username
        password = self.password

        vcs = 'svn '
        vcs_command = command + ' '

        parameter_str = ''

        for p in parameters:
            parameter_str = parameter_str + p + ' '

        options = " --non-interactive --trust-server-cert -q "

        if username is None:
            username = ''
        else:
            username = '--username ' + username + ' '

        if password is None:
            password = ''
        else:
            password = '--password ' + password + ' '


        command = vcs + vcs_command + parameter_str + options + username + password

        os.system(command)