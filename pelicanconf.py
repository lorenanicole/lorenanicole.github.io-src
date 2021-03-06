#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime 
from pathlib import Path

CURRENT_DIR_PATH = Path(__file__).resolve().parent

# Site Settings
AUTHOR = 'Lorena Mesa'
SITENAME = 'Lorena Mesa'
SITEURL = 'https://lorenamesa.com' # 'http://localhost:8000'  
THEME = '{}/voce'.format(CURRENT_DIR_PATH)
PATH = 'content'

# General Settings
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 6
SUMMARY_MAX_LENGTH = 30

# Feed Generation
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'fees/all.rss.xml'
FEED_DOMAIN = 'http://lorenamesa.com'  #'http://localhost:8000' 

# Page Settings
PAGE_SAVE_AS = '{slug}.html'
TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archive.html'

# Blogroll
LINKS = (('Home', '/index.html'),
         ('About', '/about.html'),
         ('Speaker Info', '/speaker-info.html'),
     	 ('Talks', '/talks.html'),
         ('Values', '/values.html'))

# Social Accounts
SOCIAL = (('Email', 'mailto:me@lorenamesa.com'),
          ('GitHub', 'http://github.com/lorenanicole'),
	  	  ('Twitter', 'https://twitter.com/loooorenanicole'),
	  	  ('Linkedin', 'https://www.linkedin.com/in/lorenamesa'))

# Plugins
PLUGINS = ['pelican_webassets']
PLUGIN_PATHS = ['{}/plugins'.format(THEME)]

# Publish
DELETE_OUTPUT_DIRECTORY = False

# Custom Vars
GOOGLE_ANALYTICS_ID = 'UA-124341551-1'
GOOGLE_ANALYTICS_PROP = 'Lorena Mesa Personal'
USER_LOGO_URL = 'https://www.gravatar.com/avatar/7f279cdd4dcbc3b5b98deed921ba86a2?s=500'
MANGLE_EMAILS = True
FUZZY_DATES = True
CURRENT_YEAR = datetime.now().year
ARTIST_URL = 'https://www.instagram.com/agpesty/?hl=en'

# Sitemap
SITEMAP_SAVE_AS = 'sitemap.xml'
DIRECT_TEMPLATES = ['sitemap', 'index']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
