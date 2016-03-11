# SetupBox
[![Build Status](https://travis-ci.org/maxtortime/SetupBox.svg?branch=master)](https://travis-ci.org/maxtortime/SetupBox)
## Outline
*SetupBox* is a useful middleware for implementing own storage cloud. It has multiple APIs for making the service based on version control system. We want to implement below features.

## Installation Guide
### server-side 설치를 위한 Guide - for Redhat
```sh
$ git clone https://github.com/maxtortime/SetupBox.git
$ ./server_install.sh # (superuser 권한이 필요한 작업이 있습니다. (svn, node.js, pip, virtualenv 설치))
```

현재 폴더에서 아래를 진행합니다.

```sh
#activate venv...
$ source venv/bin/activate

#install requirements
(venv) sudo pip install -r requirements.txt

#make database for user
(venv) python setupbox/web_server/db.py create_db
(venv) python setupbox/web_server/db.py db init
(venv) python setupbox/web_server/db.py db migrate
(venv) python setupbox/web_server/db.py db upgrade

#bower install
(venv) cd setupbox/web_server
(venv) bower install
(venv) cd ../..

#run server
(venv) nohup venv/bin/python setupbox/web_server/runserver.py > /dev/null &
```

## Contribution guide

###  언어
3월까지 문서에는 한국어를 사용합니다. 주석, commit log는 영어를 사용해주시기 바랍니다.

### 기여 방법
1. Collaborator: 토픽 브랜치를 만들어서 push 해주시고 코드 리뷰 후 merge하겠습니다.
2. Contributor: 프로젝트 fork 후 Pull request 해주세요.

### 브랜치 명명법
<branch name>-<issue number> 로 해주세요
ex) develop-32 , master-09, doc-23

## Demo version of server
[File manager](http://fast0.ajou.ac.kr:8080) 를 직접 체험하세요.
