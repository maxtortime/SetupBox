#!/bin/bash

CURRENT_DIR=$(pwd)
#Download and install Homebrew
echo "Check Homebrew..."
isbrew=$(brew -v)
if [ ${isbrew:0:8}="Homebrew" ]
then
	echo "Homebrew is already installed"
else
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

#install node
echo "Check node..."
isnode=$(node -v)
if [ `expr "$isnode" : "v*.*.*"` ]
then
	echo "node is already installed."
else
	brew install --silent node
fi


#install bower
echo "Check bower..."
isbower=$(bower -v)
if [ `expr "$isnode" : "*.*.*"` ]
then
	echo "bower is already installed."
else
	npm install --silent bower
fi

#install pip
echo "Check pip..."
ispip=$(pip -V)
if [ `expr "$ispip" : "pip * from *"` ]
then
	echo "pip is already installed."
else
	sudo easy_install -q pip
fi

#install virtualenv
echo "Check virtualenv..."
isvenv=$(virtualenv --version)
if [ `expr "$isvenv" : "*.*.*"` ]
then
	echo "virtualenv is already installed."
else
	sudo pip install -q virtualenv
fi

#make venv
echo "make venv..."
virtualenv venv

#activate virtualenv
echo "activate venv..."
source venv/bin/activate

#install requierments
echo "install requirements..."
sudo pip install -q -r requirements.txt

#bower install
cd setupbox/web_server
bower --silent install
cd $pwd

#run server
echo "SERVER IS RUNNING"
nohup venv/bin/python setupbox/web_server/__init__.py > /dev/null &

#open SetupBox for log-in.
open http://127.0.0.1:5000
