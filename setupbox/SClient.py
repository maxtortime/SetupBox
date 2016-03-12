from svn_wrapper import svn_wrapper
import json, sys
import requests
import time
from threading import Thread
import io
from contextlib import redirect_stdout

def update():
    while is_running:
        s.update()

        time.sleep(1)


def commit():
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
ret = resp.text.split('\n ')[0]
print(ret)
assert ret == "success", "Invalid url"

s = svn_wrapper(user_data['id'], user_data['password'])
is_running = True

s.checkout(url=user_data['repo-url'],
           dest=user_data['repo-dir'])

updater = Thread(target=update)
updater.start()

committer = Thread(target=commit)
committer.start()

updater.join()
committer.join()

# s.flush()

# s.rm('./a')

# s.update('jainersoer@ajou.ac.kr', '7004545a')

'''
           '''

# s.add('./b')

# s.commit('test', 'jainersoer@ajou.ac.kr', '7004545a')

# s.push()
