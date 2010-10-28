Proxy Hosting
=============

Proxy Hosting is a remote file server to upload html and javascript files and run them. It is able to execute AJAX calls through its internal proxy.

Installation
------------

1. Install python-virtualenv
2. $pip -E env install -r dependencies.pip
3. If you had django previously installed, execute: pip -E env install django --upgrade
4. Configure django settings in a file called settings_local.py
5. If you don't change the database config, django will use sqlite3 using a file called database.sqlite
