#!/usr/bin/env python
#import sys
from distutils.core import setup

# if sys.version < '2.5':
#     sys.exit('Python 2.5 or higher is required')

setup(name='nitm',
      version='0.1.0',
      description="""A script that tries to verify there's no MITM attacks
      between you and a web page""",
#      long_description="""""",
      license='WTFPL',
      author='myfreeweb',
      author_email='floatboth@me.com',
      url='https://github.com/myfreeweb/nitm',
      requires=['stem', 'pycurl', 'pygments', 'colorama'],
      packages=['nitm'],
      scripts=['scripts/nitm'],
      keywords=['security', 'tor', 'mitm'],
      classifiers=[
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'License :: Public Domain',
          'Environment :: Console',
          'Topic :: Security',
          'Topic :: Internet',
          'Topic :: Internet :: WWW/HTTP'
      ],
      package_data={})
