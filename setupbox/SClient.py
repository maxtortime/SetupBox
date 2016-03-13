import json
import sys
import time

import requests
from git_wrapper import git_wrapper


def common_update():
    while is_running:
        s.update()
        s.add('.')
        s.commit('syncing')
        s.push()

        time.sleep(5)

def update():
    while is_running:
        s.update()

        time.sleep(1)

def git_commit():
    while is_running:
        s.add('.')
        s.commit('syncing')
        s.push()

        time.sleep(5)

def svn_commit():
    while is_running:
        l, is_modified = s.getNewFiles()

        for e in l:
            s.add(e)

        if is_modified:
            s.commit('syncing')

        time.sleep(1)


assert len(sys.argv) == 2, "usages: python3 SClient.py user.json"

with open('user.json', 'r') as f:
    user_data = f.read()

user_data = json.loads(user_data)

resp = requests.get(user_data['auth-url'],
                    auth=(user_data['id'], user_data['password']))

print(resp.text)
print(len(resp.text))
ret = resp.text.split('\\n ')[0]
print(ret)
assert ret == "success", "Invalid url"

s = git_wrapper(user_data['id'], user_data['password'])
    # svn_wrapper(user_data['id'], user_data['password'])
is_running = True

s.checkout(url=user_data['repo-url'],
           dest=user_data['repo-dir'])

common_update()

'''
updater = Thread(target=update)
updater.start()

committer = Thread(target=git_commit)
committer.start()

updater.join()
committer.join()
'''
