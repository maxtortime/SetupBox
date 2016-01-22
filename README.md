# SetupBox
Open source cloud storage service.

SetupBox는 간단한 설치만으로 사용자에게 편리한 스토리지 클라우드 경험을 제공합니다.

내가 작업한 문서가 자동으로 서버에 전달되어 공유되고 형상 관리됩니다. 

작은 스타트업, 연구실, 가정의 중앙 서버에 저장하여 쉽게 사용하세요.

쉬운 설치, 쉬운 공유, 쉬운 버전 컨트롤!

## Youtube 링크
https://youtu.be/IGdJ-qq6d-w

## Slideshare 링크
http://www.slideshare.net/jainersoer/introduction-to-setupbox

## 구성
* SetupBox : Flask Web Server
* SetupBox_client : Linux client

## How to run server
* virtualenv와 각종 패키지를 설치하세요.
```sh
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```
* 웹서버를 구동하세요.
```sh
(venv) $ python SetupBox.py
```

## Usage of web client
* Main page
![image of MainPage](http://i.imgur.com/NbhBHK2.png)
 
* Login page 
![image of Loginpage](http://i.imgur.com/d2q63S0.png)

* Explorer 1
![Image of explorer1](http://i.imgur.com/gI1pOJh.png)

* Explorer 2
![Image of explorer2](http://i.imgur.com/YioF5lF.png)

파일을 클릭하여 삭제할 수 있고, 새로운 디렉토리를 생성할 수 있습니다.
파일을 업로드할 수 있습니다.
