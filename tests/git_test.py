# This is test code for setupbox - git
import os
from setupbox import VcsCoreGit

dir_path = '~/test_git'

#os.mkdir(os.path.expanduser(dir_path))

with open(os.path.join(os.path.expanduser(dir_path),'foo.txt'),'w') as f:
    f.write('It is test for setupbox-git')

git = VcsCoreGit(os.path.join(os.path.expanduser('~'),'test_git'))

git.commit("Initial commit")
