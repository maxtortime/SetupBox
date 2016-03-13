import uuid
from shutil import rmtree
from subprocess import Popen, PIPE

import transaction_manager as tm
from fs import clear_folder, copy_files_to, \
    get_new_files, fs, is_in_preset_dirs,\
    absjoin
from vcs import VCS

import os
from setupbox import vcs_wrapper


class svn_wrapper(vcs_wrapper):
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.vcs = None
        self.head = None

    def checkout(self, url, dest):
        self.do_command('checkout', [url, dest])
        os.chdir(dest)
        tm.initfs(dest)

        fs().preset_dirs.add(absjoin(dest, '.svn'))

        self.vcs = VCS()
        self.head = None

        self.add('.', True)
        self.commit('init')

    def add(self, targets, dont_svn_add=False):
        if is_in_preset_dirs(targets):
            return

        clear_folder(fs().stage_folder)
        copy_files_to(targets, fs().stage_folder)
        l = get_new_files(fs().current_dir,
                          fs().head_folder, fs().stage_folder)

        print('new=files', l)

        if len(l) > 0 and not dont_svn_add:
            self.do_command('add', l)
            return "new"
        return None

    def rm(self, targets):
        if is_in_preset_dirs(targets):
            return

        rmtree(absjoin(fs().stage_folder, targets))
        rmtree(absjoin(fs().current_dir, targets))

        self.do_command('rm', [targets], True)

    def commit(self, msg):
        new_uuid = str(uuid.uuid1())

        if self.head is None:
            old_uuid = new_uuid
        else:
            old_uuid = self.head.id_pointer

        assert isinstance(old_uuid, str)
        self.head = self.vcs.insert(id_pointer=new_uuid,
                                    next_pointer=new_uuid,
                                    prev_pointer=old_uuid,
                                    msg=msg)

        self.vcs.update(id_pointer=old_uuid,
                        next_pointer=new_uuid)

        new_commit_folder = absjoin(fs().commit_folder, str(new_uuid))

        if not os.path.lexists(new_commit_folder):
            os.mkdir(new_commit_folder)
        else:
            clear_folder(new_commit_folder)

        copy_files_to(fs().stage_folder, new_commit_folder)
        clear_folder(fs().stage_folder)
        clear_folder(fs().head_folder)
        copy_files_to(new_commit_folder, fs().head_folder)

    def push(self):
        self.do_command('commit', ['-m', self.head.msg if self.head is None else '\"default message\"'])

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

        print(command)

        os.system(command)
