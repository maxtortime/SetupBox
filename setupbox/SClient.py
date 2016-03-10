from svn_wrapper import svn_wrapper
import json, sys

assert len(sys.argv) == 2, "usages: python3 SClient.py user.json"

with open('user.json', 'r') as f:
    user_data = f.read()

user_data = json.loads(user_data)

import time
s = svn_wrapper(user_data['id'], user_data['passwd'])
is_running = True

def update():
    while is_running:
        s.update()

        time.sleep(1)

def commit():
    while is_running:
        s.add('.')
        s.commit()

        time.sleep(1)

from threading import Thread
updator = Thread(target=update)
updator.start()

commiter = Thread(target=commit)
commiter.start()

updator.join()
commiter.join()

# s.flush()

# s.rm('./a')

# s.update('jainersoer@ajou.ac.kr', '7004545a')

'''
s.checkout(url='https://github.com/jafffy/fast-forward-test.git',
           dest='./test')
           '''

# s.add('./b')

# s.commit('test', 'jainersoer@ajou.ac.kr', '7004545a')

# s.push()