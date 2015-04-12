#! /bin/bash

alias emacs='emacs -nw'
source /home/vagrant/dash/bin/activate

alias r='python /home/vagrant/divendash/manage.py runserver 0:8000'
pip install -r requirements.txt
