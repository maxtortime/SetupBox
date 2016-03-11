# SetupBox
[![Build Status](https://travis-ci.org/maxtortime/SetupBox.svg?branch=master)](https://travis-ci.org/maxtortime/SetupBox)
## Outline
*SetupBox* is a useful middleware for implementing own storage cloud. It has multiple APIs for making the service based on version control system.

## [LICENSE](https://github.com/maxtortime/SetupBox/blob/master/LICENSE) and [AUTHORS](https://github.com/maxtortime/SetupBox/blob/master/AUTHORS)
Please see files on the repository.

## Softwares SetupBox uses
### Libraries for Front End
* [Bootstrap](http://getbootstrap.com)
* [jQuery](https://jquery.com)
* [jQueryContextMenu](http://swisnl.github.io/jQuery-contextMenu/)
* [Flask](http://flask.pocoo.org)

### Open source software
* [bootstrap login forms](http://azmind.com/2015/04/19/bootstrap-login-forms/)

* [bootstrap registration forms](http://azmind.com/2015/03/15/bootstrap-registration-forms-3-free-responsive-templates/)

    LICENSE for above open sources :

    You can use these login form templates in personal and commercial projects, but you can’t sell or distribute them directly, “as is”. If you plan to use them, a link to this page or any form of spreading the word will be much appreciated.

* [Free file icons](https://github.com/teambox/Free-file-icons) (MIT License)

* [Simple file manager in flask](https://github.com/vmi356/filemanager) (BSD License)


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


## Contribution Guide

###  언어
3월까지 문서에는 한국어를 사용합니다. 주석, commit log는 영어를 사용해주시기 바랍니다.

### 기여 방법
1. Collaborator: 토픽 브랜치를 만들어서 push 해주시고 코드 리뷰 후 merge하겠습니다.
2. Contributor: 프로젝트 fork 후 Pull request 해주세요.

### 브랜치 명명법
<branch name>-<issue number> 로 해주세요
ex) develop-32 , master-09, doc-23

## Demo version for server-side
[File manager](http://fast0.ajou.ac.kr:8080) 를 직접 체험하세요.

## [Wiki](https://github.com/maxtortime/SetupBox/wiki)
We have wiki for our productivity and sharing information. Now, only collaborators can edit wiki. If you want to add some useful information on wiki, please register issue about that.
