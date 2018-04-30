# Music Database

Music Database for UNM CS 564 Final Project


## Contact Information

    Author: Alexander Baker
    Email: alexebaker@unm.edu
    Date: 03/26/2018


## Getting Started

1. Install Dependencies:

    Ubuntu

    ```bash
    sudo apt-get install python python-dev python-pip libssl-dev mysql-server libmysqlclient-dev
    pip install -U pip
    pip install virtualenv
    ```

    RedHat

    ```bash
    wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    yum install epel-release-latest-7.noarch.rpm
    wget https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
    yum install mysql57-community-release-el7-11.noarch.rpm
    yum install git python python-devel python-pip mysql-community-server mysql-community-client mysql-community-devel openssl openssl-devel
    pip install -U pip
    pip install virtualenv
    grep 'temporary password' /var/log/mysqld.log
    mysqladmin -u root -p password
    ```

2. Rename `auth/creds.env.example` to `auth/creds.env` and update values.

3. Setup Database:

    ```bash
    >mysql -u root -p
    >>>CREATE DATABASE music_db;
    >>>CREATE USER 'DJANGO_DB_USERNAME'@'%' IDENTIFIED BY 'DJANGO_DB_PASSWORD';
    >>>GRANT ALL PRIVILEGES ON music_db.* TO 'DJAGO_DB_USERNAME'@'%' WITH GRANT OPTION;
    >>>quit;
    >python manage.py migrate
    >python manage.py createsuperuser --username DJANGO_USERNAME # then enter your DJANGO_PASSWORD
    ```

4. This module also has several python package dependencies:

    ```bash
    virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```


## Usage

The server can be started form the command line:

```bash
python manage.py runserver 0.0.0.0:8000
```

If your browser requires ssl connections, run the sll server:

```bash
python manage.py runsslserver 0.0.0.0:8000
```
