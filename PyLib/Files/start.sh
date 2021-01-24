#!/bin/bash
echo "1) English"
echo "2) Türkçe"
read dil
if [ $dil -eq 2 ]; then
	echo "Kurulum yapılması gerekiyor. Devam edilsin mi?(1/2) "
	echo "1) Kurulum"
	echo "2) Kurma"
	read var
	if [ $var -eq 1 ]; then
		sudo apt install python3
		sudo apt install python3-pip
		pip3 install sh
		clear
		python3 then.py
	else
		exit
	fi
else
	echo "Installation is required. Continue? (1/2)"
	echo "1) Installation"
	echo "2) Nothing"
	read var
	if [ $var -eq 1 ]; then
		sudo apt install python3
		sudo apt install python3-pip
		pip3 install sh
		clear
		python3 thenEn.py
	else
		exit
	fi
fi
