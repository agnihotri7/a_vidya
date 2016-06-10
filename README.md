JobPortal
==================================

Job Portal for recruters.

# Installation

## Install OS (Ubuntu) Requirements

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install vim-gnome build-essential git-core python-dev python-virtualenv

## Clone Project

    git clone https://github.com/agnihotri7/a_vidya.git

## Virtual Envirnoment and requirements

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Project Configuartion

    touch a_vidya/local_settings.py

## MySql setup

    pip install mysql-server
    mysql -u root -p
    create database a_vidya;
    grant usage on *.* to myuser@localhost identified by 'mypasswd';
    grant all privileges on a_vidya.* to myuser@localhost;

## Edit configuration ENV for your project environment. For example:

    export ENV='test'
+ "test" (for test environment.)
+ "dev" (for development environment.)
+ "prod" (for production environment.)

## Sync database.

    python manage.py migrate

## Running Development Server

    python manage.py runserver

**Note:** Never forget to enable virtual environment (`source env/bin/activate`) before running above command and use settings accordingly.
