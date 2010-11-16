===========================
DjangoCMS SimpleNews Plugin
===========================

Provides simple news system with support for categories.

Features
========

* I18n
* Categorization
* Excerpt / full view 
* SEO (headers, slugs)

Dependencies
============

* easy-thumbnails
* django-multilingual-ng -- as of version 0.1.21 you might need to fix bugs by hand, see http://github.com/ojii/django-multilingual-ng/issues#issue/9

Easy-thumbnails will be installed automatically if using pip / easy-install.

Installation
============

Install using PIP:

  $> pip install -e git://github.com/centralniak/cmsplugin_simplenews.git#egg=cmsplugin_simplenews

Applications
------------

Register **cmsplugin_simplenews**, and these following applications in the INSTALLED_APPS section of your project's settings. ::

  >>> INSTALLED_APPS = (
  ...   # Your favorites apps
  ...   'cmsplugin_simplenews',)
  
Database 
--------

Run ./manage.py syncdb as usual.
