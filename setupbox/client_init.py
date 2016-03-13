# -*- coding: utf-8 -*-
import webbrowser
import json

with open('user.json','w') as f:
    server_addr = raw_input("Please input address notice by server manager..> ")
    user_data = dict()
    user_data['auth-url'] = server_addr + '/authTest'

    webbrowser.open(server_addr)

    email = raw_input("Please register and input your email..> ")
    password =  raw_input("Password..> ")

    user_data['id'] = email
    user_data['password'] = password
    user_data['repo-url'] = "https://github.com/jafffy/gitrepotest.git"
    user_data['repo-dir'] = '/Users/tkim/.setupbox/' + email

    f.write(json.dumps(user_data))
