from svn_wrapper import svn_wrapper
import json, sys

assert len(sys.argv) == 2, "usages: python3 SClient.py user.json"

f = open('user.json', 'r')
user_data = f.read()
f.close()
del f

user_data = json.loads(user_data)

s = svn_wrapper(user_data['id'], user_data['passwd'])

s.flush()

# s.rm('./a')

# s.update('jainersoer@ajou.ac.kr', '7004545a')

'''
s.checkout(url='https://github.com/jafffy/fast-forward-test.git',
           dest='./test')
           '''

# s.add('./b')

# s.commit('test', 'jainersoer@ajou.ac.kr', '7004545a')

# s.push()