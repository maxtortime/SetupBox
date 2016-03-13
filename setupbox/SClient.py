from svn_wrapper import svn_wrapper
import json, sys
import requests
import time

def common_update():
    while is_running:
        s.update()
        time.sleep(10)

        o = s.add('.')
        if o == "new":
            s.commit('syncing')
            s.push()

        time.sleep(10)



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

s = svn_wrapper(user_data['id'], user_data['password'])
is_running = True

s.checkout(url=user_data['repo-url'],
           dest=user_data['repo-dir'])

common_update()

