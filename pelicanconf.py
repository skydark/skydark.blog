#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Skydark Chen'
SITENAME = "Skydark's blog"
SITESUBTITLE = "Skydark 的胡言乱语"
SITESLOGAN = "This is a blog just for fun."
INDEXSLOGAN = "你看到的都是幻觉"
SITEURL = ''
DISQUS_SITENAME = 'skydblog'
LOGO = '/images/logo.jpg'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

# FIXME: which one?
DEFAULT_LANG = 'zh-CN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('远凌风', 'http://icemaple.info'),
         ('暗夜北辰', 'http://ori0n.co.de'),
         ('恶意卖萌的小师妹', 'http://www.is.pku.edu.cn/~hutingting/'),
         ('小鸠的部屋', 'http://kobato.us'),
         ('Reverland的行知阁','http://reverland.org'),)

MENUITEMS = (('关于','/about.html'),
             ('归档', '/archives.html'),
             ('Gists', '/gists.html'),
             ('留言', '/message.html'),
             ('页面', '/pages.html'),
             ('标签', '/tags.html'),
             ('工具', '/tools.html'),)
DISPLAY_PAGES_ON_MENU = False

GITHUB_USERNAME = 'skydark'
# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
          # ('Another social link', '#'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_SAVE_AS = PAGE_URL = '{slug}.html'
ARCHIVES_URL = 'archives.html'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        }

PLUGIN_PATHS = ['plugins']
PLUGINS = ['external_reader', 'mistune_reader', 'tag_cloud', 'jinja2content',
        'yamlmarkdown_reader', 'encrypt_content']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'toc']

import os
import sys
sys.path.append(os.curdir)
from extra import get_jinja_filters
JINJA_FILTERS = get_jinja_filters(MD_EXTENSIONS)

JINJA2CONTENT_TEMPLATES = ['jinja2']

TAG_CLOUD_BADGE = True
TAG_CLOUD_SORTING = 'size'

THEME = 'theme/skydark'

# --- FEED
FEED_DOMAIN = 'http://blog.skydark.info'
FEED_ATOM = 'atom.xml'
