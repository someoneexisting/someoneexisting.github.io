#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ST9001 /r/sts'
SITENAME = 'ST9001 /r/sts'
SITEURL = ''
PATH = 'content'

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


THEME = "./astrochelys"
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
PLUGINS = ['assets','pelican-toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives'))

PLUGIN_PATHS = ["./plugins"]

ADD_SEARCH_BOX = True


STATIC_PATHS = [
    "images",
]
