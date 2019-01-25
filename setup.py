import sys
if sys.version_info < (3, 0):
    sys.exit('Python 3 is required.')


from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

DESCRIPTION = """This code is updated by author to adapt to Python3. The former version of code implements a basic, Twitter-aware tokenizer. Originally developed by Christopher Potts and updated by the World Well-Being Project based out of the University of Pennsylvania and Stony Brook University. Shared with permission."""  
DISTNAME = 'happiestfuntokenizing'
LICENSE = 'GNU General Public License v3 (GPLv3)'
AUTHOR = "Christopher Potts, H. Andrew Schwartz, Maarten Sap, Salvatore Giorgi, Caspar Chan"
EMAIL = "hansens@sas.upenn.edu, sgiorgi@sas.upenn.edu"
MAINTAINER = "Caspar Chan"
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
VERSION = '0.0.6'
PACKAGES = ['happiestfuntokenizing']

if __name__ == "__main__":

  setup(name=DISTNAME,
      long_description=long_description,
      long_description_content_type='text/markdown',
      author=AUTHOR,
      author_email=EMAIL, 
      version=VERSION,
      description=DESCRIPTION,
      license=LICENSE,
      url=URL,
      download_url=DOWNLOAD_URL,
      classifiers= [
        'Environment :: Console',  
        'Natural Language :: English',  
        'Intended Audience :: End Users/Desktop',   
        'Intended Audience :: Developers',  
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        ],
      packages=PACKAGES,
    )
