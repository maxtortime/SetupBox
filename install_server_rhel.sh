#!/bin/bash

argc=$#
argv0=$0
argv1=$1

repo_name=$argv1

if [ 1 -ne $argc ]
then
	echo "Wrong argument"
	echo "./server_install.sh <repository name>"
	exit 1
fi

#install subversion
echo "Check subversion..."
issvn=$(svn --version)

if [ ${issvn:0:3}=="svn" ]
then
	echo "subversion is already installed."
else
	sudo yum install --silent svn
fi

#create repository
svnadmin create $repo_name

#install node
echo "Check node..."
isnode=$(node -v)
if [ `expr "$isnode" : "v*.*.*"` ]
then
	echo "node is already installed."
else
	sudo yum install --silent nodejs
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
	echo "Downloadig get-pip.py..."
	curl --silent -o get-pip.py https://bootstrap.pypa.io/get-pip.py
	sudo python get-pip.py
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

