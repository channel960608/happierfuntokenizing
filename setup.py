from setuptools import setup

DESCRIPTION = """This code is updated by Auther to adapt to Python3. The former version of code implements a basic, Twitter-aware tokenizer. Originally developed by Christopher Potts and 
updated by the World Well-Being Project based out of the University of Pennsylvania and Stony Brook University. Shared with permission."""

DISTNAME = 'happiestfuntokenizing'
LICENSE = 'GNU General Public License v3 (GPLv3)'
AUTHOR = "Christopher Potts, H. Andrew Schwartz, Maarten Sap, Salvatore Giorgi, Caspar Chan"
EMAIL = "hansens@sas.upenn.edu, sgiorgi@sas.upenn.edu"
MAINTAINER = "Caspar Cgab"
MAINTAINER_EMAIL = "channel960608@gmail.com"
URL = 'http://dlatk.wwbp.org'
DOWNLOAD_URL = 'https://github.com/channel960608/happiestfuntokenizing'
CLASSIFIERS = [
  'Environment :: Console',
  'Natural Language :: English',
  'Intended Audience :: End Users/Desktop',
  'Intended Audience :: Developers',
  'Intended Audience :: Science/Research',
  'Programming Language :: Python',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 3.6',
  'Topic :: Scientific/Engineering',
]
VERSION = '0.0.2'

if __name__ == "__main__":

  setup(name=DISTNAME,
      author=AUTHOR,
      author_email=EMAIL, 
      version=VERSION,
      description=DESCRIPTION,
      license=LICENSE,
      url=URL,
      download_url=DOWNLOAD_URL,
      classifiers=CLASSIFIERS,
  )
