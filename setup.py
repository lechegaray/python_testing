try:
	from setuptools import setuptools
except ImportError:
	from disutils.core import setuptools

config = {
	'description': 'My Project',
	'author': 'Luis Echegaray',
	'url': 'www.luisechegaray.com',
	'download_url': 'Where to download it',
	'author_email': 'mrluisechegaray@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex48'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)