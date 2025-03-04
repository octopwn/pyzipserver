from setuptools import setup, find_packages
import re

VERSIONFILE="pyzipserver/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
	# Application name:
	name="pyzipserver",

	# Version number (initial):
	version=verstr,

	# Application author details:
	author="Tamas Jos",
	author_email="info@octopwn.com",

	# Packages
	packages=find_packages(),

	# Include additional files into the package
	include_package_data=True,


	# Details
	url="https://github.com/octopwn/pyzipserver",

	zip_safe = False,
	#
	# license="LICENSE.txt",
	description="",

	# long_description=open("README.txt").read(),
	python_requires='>=3.7',
	install_requires=[],
	
	classifiers=(
		"Programming Language :: Python :: 3.7",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	),
	entry_points={
		'console_scripts': [
			'pyzipserver = pyzipserver.server:main',
		],
	
	}
)