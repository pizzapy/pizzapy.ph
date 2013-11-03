#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marconi Moreto'
SITENAME = u'Pizzapy'
SITEURL = 'http://pizzapy.ph'

TIMEZONE = 'Asia/Hong_Kong'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Want to sponsor our next meetup?', 'mailto:admin@pizzapy.ph'),
          ('Follow us @pizzapyph', 'https://twitter.com/pizzapyph'))

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

THEME = 'themes/chicken-and-pesto'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MENUITEMS = (
    ('Meetups', 'users', '/category/meetups.html'),
    ('Archive', 'archive', '/category/archive.html'),
    ('Talk Submission', 'chat', '/pages/talk-submission.html'),
    ('Sponsorship', 'tint', '/pages/sponsorship.html'),
    ('About', 'help', '/pages/about.html'),
)

TWITTER = ('@pizzapyph', 'https://twitter.com/pizzapyph')
