#!/bin/bash
apt install postgresql
su - postgres
createuser pi -P --interactive
psql -c 'CREATE DATABASE pi;'
exit
su - pi
psql -f install_script.sql
psql -c 'CREATE DATABASE sensordb;'
psql sensordb -c 'CREATE TABLE temperature (date timestamp, celsius int, humidity int);' 
exit
