###
### Author: Asya Kamsky
###

from setuptools import setup

if __name__ == '__main__':
    setup(name='yam_fdw',
          author='Asya Kamsky',
          author_email='asya@kamsky.org',
          description='Yet Another Postgres FDW for MongoDB',
          url='http://github.com/asya999/yam_fdw',
          version='0.7.1',
          install_requires=['pymongo>=2.8.1',
                            'python-dateutil'],
          packages=['yam_fdw'])

## Local Variables: ***
## mode:python ***
## coding: utf-8 ***
## End: ***
