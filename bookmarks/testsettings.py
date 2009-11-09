DEBUG = True
DEBUG_TEMPLATE = True
SITE_ID = 1
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/asgard-bookmarks-devel.db'
INSTALLED_APPS = [
	'django.contrib.auth',
	'django.contrib.comments',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.admin',
	'django.contrib.sites',
	'django.contrib.sitemaps',
	
	'tagging',
	
	'asgard.bookmarks',
]
ROOT_URLCONF = 'asgard.bookmarks.testurls'